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
       
		
		stage('Trigger ManifestUpdate') {
		    steps{
			
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
				}
				}
    }
}
