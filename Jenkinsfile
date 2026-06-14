pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
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
    }
}