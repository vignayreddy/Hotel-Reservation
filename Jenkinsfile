pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "project-82ee730d-c76d-4cc9-b7b"
        GCLOUD_PATH = "/opt/gcloud/bin"
    }

    stages {

        stage('Clone Repo') {
            steps {
                echo 'Cloning Github repo...'
                checkout scmGit(
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/vignayreddy/Hotel-Reservation.git']]
                )
            }
        }

        stage('Setup Virtual Environment & Install Dependencies') {
            steps {
                sh '''
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -e .
                '''
            }
        }

        stage('Train Model') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                    . ${VENV_DIR}/bin/activate
                    python pipeline/training_pipeline.py
                    '''
                }
            }
        }

        stage('Build & Push Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                    export PATH=$PATH:/opt/gcloud/bin

                    echo "Authenticating GCP..."
                    gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

                    gcloud config set project $GCP_PROJECT

                    gcloud auth configure-docker --quiet

                    echo "Building Docker image..."
                    docker build -t gcr.io/$GCP_PROJECT/ml-project:latest .

                    echo "Pushing Docker image..."
                    docker push gcr.io/$GCP_PROJECT/ml-project:latest
                    '''
                }
            }
        }
    }
}