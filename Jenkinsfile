pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
        GCP_PROJECT = "project-82ee730d-c76d-4cc9-b7b"
        GCLOUD_PATH ="/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins..............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vignayreddy/Hotel-Reservation.git']])

                }
            }
        }
         stage('Setting up the virtual Environment and Installing Dependancies'){
            steps{
                script{
                    echo 'Setting up the virtual Environment and Installing Dependancies...............'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''

                }
            }
        }
        stage('Building and Pusing  Docekr Image to GCR'){
            steps{
                
                withCredentials([file(credentialsId : 'gcp-key',variable:'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and Pusing  Docekr Image to GCR..............'
                        sh '''
                        export PATH=$PATH:$(GCLOUD_PATH)

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest 
                        
                        '''
                    }
                }
            }
        }




    }
}