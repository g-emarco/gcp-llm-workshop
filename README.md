# GCP RAG (Retrieval Augmentation Generation) Vectorstore workshop - PGVector

Final Product: Chat with your Data (Scrape public websites/ your PDFs) GenAI project

This repository is designed for a workshop teach the concept of in context learning and working with vectirstires (pgvector)
when building GenAI applications with LangChain.


![Alt Text](https://github.com/g-emarco/github-assistant/blob/main/static/demo21.gif)


## Tech Stack


**Server Side:** LangChain  🦜🔗

**Vectorstore:** Postgres PGVector 

**Embeddings:** GCP VertexAI  

**LLM:** PaLM 2



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DB_URL`
`APPLICATION_DEFAULT_CREDENTIALS`

## Run Locally


Clone the project

```bash
  git clone https://github.com/emarco177/gcp-llm-workshop.git
```

Go to the project directory

```bash
  cd gcp-llm-workshop
```

Install dependencies

```bash
  pipenv install
```

Start the Streamlit server

```bash
  python3 run rag/ingestion.py
  python3 run rag/retrieval_aguentation.py
```

NOTE: When running locally make sure `GOOGLE_APPLICATION_CREDENTIALS` is set to a service account with permissions to use VertexAI


## GCP SETUP


Please replace $PROJECT_ID with your actual Google Cloud project ID.

To deploy manually:

1. Make sure you enable GCP APIs:

```bash
gcloud services enable vertexai.googleapis.com

```

2. Create a service account `vertex-ai-consumer` with the following roles:



```bash
gcloud iam service-accounts create vertex-ai-consumer \
    --display-name="Vertex AI Consumer"
    

gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:vertex-ai-consumer@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/serviceusage.serviceUsageConsumer"

gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:vertex-ai-consumer@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/ml.admin"

gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:vertex-ai-consumer@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/vertexai.admin"
```


## 🚀 About Me
Eden Marco, Customer Engineer @ Google Cloud, Tel Aviv🇮🇱

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eden-marco/) 

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/EdenEmarco177)

