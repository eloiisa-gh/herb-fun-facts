import os

from flask import Flask

app = Flask(__name__)

# This code responds to http requests with our HelloWorld greeting
@app.route("/")
def hello_world():
    return f"HelloWorld from main py (homepath route)"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))