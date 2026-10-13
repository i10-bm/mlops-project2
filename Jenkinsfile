@Library('jenkins-shared-library') _

pipeline {
    agent any
    environment {
        MLFLOW_TRACKING_URI = 'http://127.0.0.1:5000'
    }
    stages {
        stage('Route Branch Pipeline') {
            steps {
                script {
                    if (TAG_NAME =~ /^v\d+\.\d+/) {
                        prodPipeline()
                    } else if (BRANCH_NAME == 'main') {
                        preProdPipeline()
                    } else if (BRANCH_NAME == 'dev') {
                        devPipeline()
                    }
                }
            }
        }
    }
}
