# Gen AI + Python / Herbs Information 🌿

This [website](https://codelab-genai-python-95958779617.europe-west1.run.app/) shows 11 interesting facts about an herb. Eg: [oregano](https://codelab-genai-python-95958779617.europe-west1.run.app?herb=thyme). Try it with [other herbs](https://www.britannica.com/plant/list-of-herbs-and-spices-2024392). 

`URL`/?herb=`HERB_NAME`

Model used: `gemini-2.5-flash`: [Gemini 2.5 Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash)


<details >
  <summary>More details</summary>

Continuous deployment: [Cloud Run](https://cloud.google.com/run) is configured to automatically deploy the web application when the source code is changed. 
Generative AI was added to the application using Vertex AI. 

Based on: [Automatically Deploy Generative AI Python Web Application from Version Control to Cloud Run](https://codelabs.developers.google.com/codelabs/deploy-from-github/gen-ai-python)


In the Google Cloud CLI, check the active authenticated gcloud account: 
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
https://codelab-genai-python-95958779617.europe-west1.run.app/


</details>
