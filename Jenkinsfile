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
                    ansiColor('xterm') {
                        if (fileExists("${DATASET_DIR}/main.py")) {
                            sh "jupytext --to notebook ${DATASET_DIR}/*.py"
                        }
                        sh "jupyter-nbconvert --output-dir=${DATASET_DIR}/out --ExecutePreprocessor.timeout=None --execute '${DATASET_DIR}/main.ipynb'"
                        }
                   }
                }
            }
        } 
    }
}

