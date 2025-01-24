import os

import sys, json, logging

class JsonFormatter(logging.Formatter):
    def format(self, record):
        json_log_object = {
            "severity": record.levelname,
            "message": record.getMessage(),
        }
        json_log_object.update(getattr(record, "json_fields", {}))
        return json.dumps(json_log_object)
logger = logging.getLogger(__name__)
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(JsonFormatter())
logger.addHandler(sh)
logger.setLevel(logging.DEBUG)

from flask import Flask, request

import google.auth
import vertexai
from vertexai.generative_models import GenerativeModel

_, project = google.auth.default()

app = Flask(__name__)

@app.route("/")
def hello_world():
    vertexai.init(project=project, location="us-central1")
    model = GenerativeModel("gemini-1.5-flash")
    herb = request.args.get("herb", "basil") 
    prompt = f"Give me 11 interesting facts about {herb}. Return this as html without backticks."
    response = model.generate_content(prompt)

    json_fields = {"prompt": prompt, "response": response.to_dict()}
    logger.debug("Content is generated", extra={"json_fields": json_fields})

    return response.text

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))