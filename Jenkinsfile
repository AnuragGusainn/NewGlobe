pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = 'lessoncompletion-api'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AnuragGusainn/NewGlobe.git/lessoncompletion-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}:${BUILD_NUMBER}").inside {
                        sh 'pytest'  // Run your test command
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'DOCKERHUB_CREDENTIALS') {
                        docker.image("${IMAGE_NAME}:${BUILD_NUMBER}").push()
                    }
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}:${BUILD_NUMBER}").run('-p 5000:5000')
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                input message: "Approve deployment to production?", ok: "Deploy"
                script {
                    docker.image("${IMAGE_NAME}:${BUILD_NUMBER}").run('-p 80:5000')
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
