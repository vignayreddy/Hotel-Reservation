# 🏨 Hotel Reservation Cancellation Prediction (MLOps)

This repository contains an end-to-end MLOps pipeline designed to predict whether a customer will honor or cancel their hotel reservation. The system leverages cloud data storage, robust model tracking, automated CI/CD pipelines, and serverless container deployment.

---

## 🏗️ System Architecture & Workflow

1. **Data Layer:** Raw reservation data is managed via automated ETL flows and stored securely in a Google Cloud Storage bucket.
2. **Experimentation:** Version control handles small tracking files while heavy assets are tracked via DVC. Models are monitored across iterations using an MLflow tracking server.
3. **Continuous Integration & Deployment:** Commits to GitHub trigger automated Jenkins pipelines. Jenkins builds a Docker image via Docker-in-Docker (DinD), registers it to Google Container Registry (GCR), and ships it to Google Cloud Run.

---

## 📁 Repository Directory Structure

```text
├── src/                      # Source code modules (Ingestion, Preprocessing, Training)
├── notebook/                 # Jupyter Notebooks for EDA and prototype testing
├── templates/                # HTML files for the Flask UI
├── static/                   # CSS and JavaScript assets
├── config/                   # Configuration files (config.yaml, model_params.yaml)
├── artifacts/                # Local data splits and serialized model outputs
├── pipeline/                 # Training and prediction orchestration scripts
├── utils/                    # Common helper utilities
├── Dockerfile                # Project container definition
├── requirements.txt          # Python dependencies
└── setup.py                  # Project package installation settings
```

---

## ⚙️ Local Development Setup

### 1. Environment Initialization

Isolate your development dependencies by initializing a clean virtual environment:

```bash
python -m venv venv
```

Activate the environment:

| OS | Command |
|----|---------|
| Windows (PowerShell) | `venv\Scripts\activate` |
| Linux / macOS | `source venv/bin/activate` |

### 2. Dependency Installation

Install required libraries (including `imbalanced-learn`) and package the source directory in editable mode:

```bash
pip install -r requirements.txt
pip install -e .
```

---

## ☁️ Google Cloud Platform Configuration

### 1. Service Account Authorization

To extract files from Cloud Storage, establish valid authentication configurations:

1. Go to the GCP Console and navigate to **IAM & Admin → Service Accounts**.
2. Create a service account with the **Storage Admin** and **Storage Object Viewer** roles.
3. Whitelist the service account email within your target Cloud Storage bucket permissions panel.

### 2. Local Key Generation Fallback

If you encounter permission blockers or errors while downloading JSON keys from the console, authenticate locally via the Google Cloud CLI:

```bash
gcloud auth application-default login
```

This maps credentials locally to:

```
C:\Users\vigna\AppData\Roaming\gcloud\application_default_credentials.json
```

---

## 📊 Pipeline Orchestration

### Data Ingestion & Preprocessing

- Run the ingestion module to extract the dataset from your GCP bucket and execute a structured train-test split.
- Add `data_preprocessing` parameters to `config/config.yaml`.
- Use preprocessing routines to balance target distribution flags using `imbalanced-learn`.

### Experiment Tracking with MLflow

Configure model training hyperparameters inside `config/model_params.yaml`. To launch your experiment tracker and compare iterations, spin up the MLflow server:

```bash
mlflow ui
```

Dashboard URL: `http://127.0.0.1:5000`

---

## 🚀 CI/CD Automation via Jenkins & Cloud Run

The deployment pipeline relies on a custom **Docker-in-Docker (DinD)** Jenkins image to assemble runtime environments.

### 1. Build the Custom Jenkins Automation Image

```bash
cd custom_jenkins
docker build -t jenkins-dind .
```

### 2. Deploy the Jenkins Container

Launch your local automation server with exposed web management ports:

```bash
docker run -d --name jenkins-dind -p 8080:8080 -p 50000:50000 jenkins-dind:latest
```

### 3. Deployment Steps

1. Connect Jenkins to your **GitHub** repository webhook.
2. Configure your pipeline stage to login to Docker, assemble your Flask web app image, and push it directly to the **Google Container Registry (GCR)**.
3. Extract the freshly built image from GCR and deploy it directly onto **Google Cloud Run** for public serverless hosting.

> ⚠️ **Important:** Ensure that the **Artifact Registry API** and **Cloud Resource Manager API** are enabled within your GCP Project console prior to executing the build pipeline.

---

## 📋 Prerequisites Summary

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core runtime |
| Docker | Containerization & local Jenkins |
| Google Cloud SDK | GCP authentication & deployment |
| MLflow | Experiment tracking |
| DVC | Large file / data versioning |
| Jenkins | CI/CD automation |
