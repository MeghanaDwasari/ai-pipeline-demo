pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the AI project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Validating model accuracy...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying AI model to production...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
        always {
            archiveArtifacts artifacts: 'result.txt', allowEmptyArchive: true
        }
    }
}
