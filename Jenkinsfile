pipeline {
    agent {dockerfile true}

    environment {
        DOCKERHUB_CREDS = credentials('dockerhub')
    }

    stages {
        stage('git clone') {
            steps {
                 sh 'git clone -b main https://github.com/jubick1337/mle_hw1.git'
            }
        }

        stage('check folder') {
            steps {
                sh 'cd mle_hw1 && ls'
            }
        }

        stage('docker auth'){
            steps {
                sh 'docker login -u %DOCKERHUB_CREDS_USR% -p %DOCKERHUB_CREDS_PSW%'
            }
        }

        stage('build') {
            steps {
                 sh  "cd mle_hw1 && docker-compose build"
            }
        }

        stage('check log'){
            steps{
                  sh 'docker-compose logs'
            }
        }

        stage('push container'){
            steps{
                sh 'docker push jubick/mle_hw1:latest'
            }
        }
    }

    post {
		always {
			sh 'docker logout'
		}
	}
}