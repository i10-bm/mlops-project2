@Library('jenkins-shared-library@main') _

pipeline {
    agent any

    stages {
        stage('Route Branch Pipeline') {
            steps {
                script {
                    if (env.TAG_NAME) {
                        prodPipeline()
                    } else if (env.BRANCH_NAME == 'main') {
                        preProdPipeline()
                    } else if (env.BRANCH_NAME == 'dev') {
                        devPipeline()
                    } else {
                        echo "Unknown branch or tag: ${env.BRANCH_NAME}"
                    }
                }
            }
        }
    }
}
