pipeline {
    agent {
        label 'master'
    }
    environment {
        DATASET_DIR = "datasets/${JOB_BASE_NAME}"
    }
    stages {
        stage('Clean') {
            steps {
                sh "rm -rf ${DATASET_DIR}/out"
            }
        }
        stage('Transform') {
            agent {
                docker {
                    image 'gsscogs/databaker'
                    reuseNode true
                    alwaysPull true
                }
            }
            steps {
                withCredentials([string(credentialsId: 'github_token', variable: 'SECRET')]) { //set SECRET with the credential content
                  script {
                    if (fileExists("${DATASET_DIR}/main.py")) {
                            sh "python ${DATASET_DIR}/*.py"
                    }
                    }
                }
            }
        } 
    }
}

