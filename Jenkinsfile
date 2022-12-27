pipeline {
    agent any

    environment {
        dockerhub = credentials('dockerhub')
    }

    stages {
        stage('check folder') {
            steps {
                sh 'ls'
            }
        }

        stage('check'){
            steps{
                sh 'echo $dockerhub_USR'
            }
        }

        stage('docker auth'){
            steps {
                sh 'echo Sdockerhub_PSW | docker login -u Sdockerhub_USR --password-stdin'
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
                 sh  "docker-compose build"
            }
        }

        stage('check log'){
            steps{
                  sh 'docker-compose logs'
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