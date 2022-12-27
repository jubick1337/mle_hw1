pipeline {
    agent any

    environment {
        dockerhub = credentials('dockerhub')
    }

    options {
        disableConcurrentBuilds()
    }

    stages {
        stage('login'){
            steps{
                  sh 'echo ${dockerhub_PSW} | docker login -u ${dockerhub_USR} --password-stdin'
            }
        }

        stage ('build'){
            steps{
                sh 'docker build -f Dockerfile -t mle_hw:latest .'
            }
        }

        stage ('tag'){
            steps{
                sh 'docker tag mle_hw jubick/mle_hw'
            }
        }

        stage('compose') {
            steps {
                 sh  "docker compose up"
            }
        }

        stage('push container'){
            steps{
                sh 'docker push jubick/mle_hw:latest'
            }
        }
    }

    post {
		always {
			sh 'docker logout'
		}
	}
}