# 🏨 Hotel Reservation Project

## 📦 Database Setup

* Create a **Google Cloud Storage bucket** in your project.
* Upload the **hotel reservation dataset** into the bucket.

---

## ⚙️ Project Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -e .
```

> This command automatically checks and installs dependencies defined in `setup.py`.

---

## ☁️ Google Cloud Configuration

### 1. Verify Google Cloud SDK

```bash
gcloud --version
```

---

## 🔐 Service Account Setup

1. Go to **IAM & Admin → Service Accounts**
2. Create or select a service account
3. Assign the following roles:

   * **Storage Admin**
   * **Storage Object Viewer**

---

## 🪣 Bucket Permissions

1. Navigate to **Cloud Storage → Buckets**
2. Select your bucket (e.g., `hotel-reservation`)
3. Go to **Permissions (Principals)**
4. Add the service account:

   ```
   hotel-reservation@project-82ee730d-c76d-4cc9-b7b.iam.gserviceaccount.com
   ```
5. Assign the same roles:

   * Storage Admin
   * Storage Object Viewer

---

## 🔑 Authentication Setup

1. Go to **Service Accounts**
2. Select your service account
3. Generate a **Key (JSON format)**

---

## ⚠️ Fix for Key Generation Error

If key generation fails, run:

```bash
gcloud auth application-default login
```

This creates credentials at:

```
C:\Users\vigna\AppData\Roaming\gcloud\application_default_credentials.json
```

> ✅ This file is sufficient to establish a secure connection between your local environment and Google Cloud for data access.

---

## 📥 Data Ingestion

* Use the configured service account and credentials
* Access the dataset directly from the cloud bucket
* Implementation details can be found in the **Data Ingestion module**


## Data Preprocessing
* import all modules required into the data_preprocesijnga nd also add data_preprocessing in congif_yaml file
instakk imbalanced learn from requiremtns,txt
complete all steps as followed ..

##Model Training 


*  create model_parans in config folder for storing model parameters...



 MlFLOW Used for experiment tracking 
* mlflow ui
<!-- http://127.0.0.1:5000 -->


* Training pipeline and Data & code versioning


* User App building using Flask and chatgpt

* CI-CD Deployment using jenkins and Google Clo
ud Run


project->github->google cloud 

1) setup jenkins container
2) Github Integration
3) Dockerization of project
4) Create a venv in your jenkins
5) Build Docker Image of yout project - > push to GCR (Google Cloud Registry)
6) Extract the image from GCR -> Push to Google Cloud Run




DinD -> Docker in Docker


(venv) PS C:\Users\vigna\Desktop\HotelReservation\custom_jenkins> docker login
Authenticating with existing credentials... [Username: vignayreddy]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
(venv) PS C:\Users\vigna\Desktop\HotelReservation\custom_jenkins> 

docker build -t jenkins-dind .
(venv) PS C:\Users\vigna\Desktop\HotelReservation\custom_jenkins> docker build -t jenkins-dind .
[+] Building 65.5s (7/7) FINISHED                                   docker:desktop-linux
 => [internal] load build definition from Dockerfile                                0.0s
 => => transferring dockerfile: 211B                                                0.0s
 => [internal] load metadata for docker.io/jenkins/jenkins:lts                      1.0s
 => [internal] load .dockerignore                                                   0.0s
 => => transferring context: 2B                                                     0.0s
 => CACHED [1/3] FROM docker.io/jenkins/jenkins:lts@sha256:01c992ffef29dcf41c7164e  0.0s
 => => resolve docker.io/jenkins/jenkins:lts@sha256:01c992ffef29dcf41c7164e8c16285  0.0s
 => [2/3] RUN apt-get update &&     apt-get install -y docker.io &&     apt-get c  43.7s
 => [3/3] RUN usermod -aG docker jenkins                                            0.3s 
 => exporting to image                                                             20.3s 
 => => exporting layers                                                            17.0s 
 => => exporting manifest sha256:90f55f5527dca38d97bf4cf0e7162048d592943aee8229c00  0.0s 
 => => exporting config sha256:8981d23b65db7b343459ed2bca09a71c701f2a6b6de34d76c71  0.0s 
 => => exporting attestation manifest sha256:b3e28e5b1111b4eb9b613f505e5c66bcd2568  0.0s 
 => => exporting manifest list sha256:5ef383fdbef540a0e5496b3e026870073a737cc80f7c  0.0s
 => => naming to docker.io/library/jenkins-dind:latest                              0.0s
 => => unpacking to docker.io/library/jenkins-dind:latest                           3.2s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/wqcwotvt78aofy0fp6g7ha6ti
(venv) PS C:\Users\vigna\Desktop\HotelReservation\custom_jenkins> 
(venv) PS C:\Users\vigna\Desktop\HotelReservation\custom_jenkins> 
(venv) PS C:\Users\vigna\Desktop\HotelReservation\custom_jenkins> docker images
REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
jenkins-dind             latest    5ef383fdbef5   46 seconds ago   1.41GB
vignay/welcome-app       latest    fe4c68f3b86c   6 months ago     92.9MB
redis                    latest    43355efd2249   6 months ago     202MB
hello-world              latest    f7931603f70e   9 months ago     20.3kB
docker/getting-started   latest    d79336f4812b   3 years ago      73.9MB
(venv) PS C:\Users\vigna\Desktop\HotelReservation\custom_jenkins> 

MB
(venv) PS C:\Users\vigna\Desktop\HotelReservation\custom_jenkins> docker run -d --name jenkins-dind -p 8080:8080 -p 50000:50000 jenkins-dind:latest
6c0b3bef3c9222e7014b362dacd833abb720a7c7c3ba2da80a2e9d6dab50879f


# go to gcr and turn it enabled


54:53 -- Artifact Registry API
Cloud Resource Manager API