# Herb Fun Facts 🌿

This [website](https://herb-fun-facts-95958779617.europe-west1.run.app/) shows 11 interesting facts about an herb. 
This parameter can also be provided in this way: `URL`/?herb=`HERB_NAME`

Eg: [thyme](https://herb-fun-facts-95958779617.europe-west1.run.app?herb=thyme). Try it with [other herbs](https://www.britannica.com/plant/list-of-herbs-and-spices-2024392). 

Model used: `gemini-2.5-flash`: [Gemini 2.5 Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash)


<details >
  <summary>Instructions</summary>

Continuous Deployment: [Cloud Run](https://cloud.google.com/run) is configured to automatically deploy the web application when the source code is changed. 
Generative AI was added to the application using Vertex AI.

Based on: [Automatically Deploy Generative AI Python Web Application from Version Control to Cloud Run](https://codelabs.developers.google.com/codelabs/deploy-from-github/gen-ai-python)


<details open>
  <summary>Project setup</summary>

### Project setup

In the Google Cloud CLI, check the active authenticated gcloud account: 
```
gcloud auth list
```

Set your project: 
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
</details>


### Set up automatic deployments
To automatically deploy this Generative AI Python Web Application from Version Control to Cloud Run: 

In the [Cloud Run page](https://console.cloud.google.com/run), select 'Create service', 'Continuously deploy from a repository (source or function)'. Click 'Set up with Cloud Build'. 

Step #1: Select the 'Source repository'. 
Step #2: 'Build Configuration' -> 'Build Type': `Go, Node.js, Python, Java, .NET Core, Ruby or PHP via Google Cloud's buildpacks`. 

In the 'Configure' section, set the 'Service name' eg: `herb-fun-facts`, and 'Region'. 
In 'Authentication', select `Allow unauthenticated invocations`. 

Click 'Create'.


To get the resulting URL to view the running application: 
```
gcloud run services list
```
https://herb-fun-facts-95958779617.europe-west1.run.app/


</details>
