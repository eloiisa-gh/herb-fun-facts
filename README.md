# Gen AI for Python Developers

This [website](https://codelab-genai-python-412316639419.us-central1.run.app/) shows 11 interesting facts about an herb. Eg: [oregano](https://codelab-genai-python-412316639419.us-central1.run.app/?herb=oregano)

<details >
  <summary>More details</summary>

  [Automatically Deploy Generative AI Python Web Application from Version Control to Cloud Run](https://codelabs.developers.google.com/codelabs/deploy-from-github/gen-ai-python)

Continuous deployment: [Cloud Run](https://cloud.google.com/run) is configured to automatically deploy the web application when the source code is changed. 
Generative AI was added to the application using Vertex AI (Gemini 1.5 Flash). 


Google Cloud CLI: 
```
gcloud auth list                                                     
```

Create a Cloud project
```
gcloud projects create PROJECT_ID
gcloud projects list
```

### Enable billing for your Cloud project
List available billing accounts: 
```
gcloud billing accounts list
```

Link a billing account with a Google Cloud project: 
```
gcloud billing projects link PROJECT_ID --billing-account=BILLING_ACCOUNT_ID
```

### Set your project
```
gcloud config set project PROJECT_ID
```

Enable APIs: 
```
gcloud services enable \
  run.googleapis.com \
  cloudbuild.googleapis.com \
  aiplatform.googleapis.com
```

List the services a project has enabled for consumption: 
```
gcloud services list --enabled --project=PROJECT_ID
gcloud services list --enabled --project=${GOOGLE_CLOUD_PROJECT}
```

Open the main.py file in Cloud Shell Editor:
```
cloudshell edit main.py
```


### Set up automatic deployments
In the [Cloud Run page](https://console.cloud.google.com/run), click 'Connect repo' and Click 'Set up with Cloud Build'. 

Step #1: 'Source repository'. 
In step #2: 'Build Configuration', select Build Type: 'Go, Node.js, Python, Java, .NET Core, Ruby or PHP via Google Cloud's buildpacks'. 

In 'Authentication', select 'Allow unauthenticated invocations'. 
Click 'Create'.


To get the resulting URL to view the running application: 
```
gcloud run services list
```

</details>
