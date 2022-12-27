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
// steps{
//       withCredentials([string(credentialsId: 'DockerHubPwd', variable: 'dockerpwd')]) {
//       sh "docker login -u username -p ${dockerpwd}"
//             }
//         }
        stage('check log'){
            steps{
                  sh 'docker compose logs'
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