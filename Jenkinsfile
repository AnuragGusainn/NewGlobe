pipeline {
    agent any 
    
    stages {
        stage("Clone Code") {
            steps {
                echo "Cloning the code"
                git url: "https://github.com/AnuragGusainn/NewGlobe.git", branch: "master"
            }
        }
        stage("Build") {
            steps {
                echo "Building the image"
                sh "docker build -t flask-app ."
            }
        }
        stage("Push to Docker Hub") {
            steps {
                echo "Pushing the image to Docker Hub"
                withCredentials([usernamePassword(credentialsId: "DockerUname", passwordVariable: "dockerHubPass", usernameVariable: "dockerHubUser")]) {
                    // Tagging with 'latest' and build number
                    sh "docker tag flask-app ${env.dockerHubUser}/flask-app:latest"
                    sh "docker tag flask-app ${env.dockerHubUser}/flask-app:${env.BUILD_NUMBER}"
                    
                    // Logging in to Docker Hub
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    
                    // Pushing both 'latest' and build-numbered tags
                    sh "docker push ${env.dockerHubUser}/flask-app:latest"
                    sh "docker push ${env.dockerHubUser}/flask-app:${env.BUILD_NUMBER}"
                }
            }
        }
       
        stage('Trigger ManifestUpdate') {
            steps {
                echo "Triggering updatemanifest job"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
            }
        }
    }
}
