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

