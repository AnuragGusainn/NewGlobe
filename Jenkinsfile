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
                    sh "docker tag flask-app ${env.dockerHubUser}/flask-app:latest"
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    sh "docker push ${env.dockerHubUser}/flask-app:latest"
                }
            }
        }
        stage("Deploy to Kubernetes") {
            steps {
                echo "Deploying to Kubernetes"
                
                // Set Kubernetes context if needed
                // sh "kubectl config use-context YOUR_CONTEXT"

                // Apply deployment and service YAML files
                sh "kubectl apply -f deployment.yaml"
                sh "kubectl apply -f service.yaml"

                // Optionally, check the status of the deployment
                sh "kubectl rollout status deployment/flask-app" // Replace with your deployment name
            }
        }
		
		stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
				}
    }
}
