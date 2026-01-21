pipeline {
    agent any

    parameters {
        choice(
            name: 'DEPLOY_ENV',
            choices: ['dev', 'staging', 'prod'],
            description: 'Select environment'
        )

        string(
            name: 'APP_VERSION',
            defaultValue: '1.0.0',
            description: 'Application version'
        )
    }

    stages {
        stage('Build') {
            steps {
                echo "Building version ${params.APP_VERSION}"
            }
        }

        stage('Prod Approval') {
            when {
                expression { params.DEPLOY_ENV == 'prod' }
            }
            steps {
                input message: 'Approve production deployment?', ok: 'Deploy'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (params.DEPLOY_ENV == 'dev') {
                        echo "Deploying to DEV environment"
                    }
                    else if (params.DEPLOY_ENV == 'staging') {
                        echo "Deploying to STAGING environment"
                    }
                    else {
                        echo "Deploying to PRODUCTION environment"
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Deployment completed for ${params.DEPLOY_ENV}"
        }
    }
}
