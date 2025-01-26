# Gen AI for Python Developers

This [website](https://codelab-genai-python-412316639419.us-central1.run.app/) shows 11 interesting facts about an herb. Eg: [oregano](https://codelab-genai-python-412316639419.us-central1.run.app/?herb=oregano)

<details >
  <summary>More details</summary>

  [Automatically Deploy Generative AI Python Web Application from Version Control to Cloud Run](https://codelabs.developers.google.com/codelabs/deploy-from-github/gen-ai-python)

Continuous deployment: [Cloud Run](https://cloud.google.com/run) is configured to automatically deploy the web application when the source code is changed. 
Generative AI was added to the application using Vertex AI (Gemini 1.5 Flash). 


To enable APIs: 
```
gcloud services enable \
  run.googleapis.com \
  cloudbuild.googleapis.com \
  aiplatform.googleapis.com
```

To list the services a project has enabled for consumption: 
```
gcloud services list --enabled --project=${GOOGLE_CLOUD_PROJECT}
```

</details>
