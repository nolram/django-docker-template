pipeline{
    agent any
    stages {
        stage('Clone repository') {
            steps{
                checkout scm
            }
        }
        stage('Build'){
            steps{
                sh 'git archive -o django-template.tar HEAD'
                sh 'docker build -t nolram/django-template:latest --rm -f Dockerfile.prod .'
            }
        }
        stage('Test'){
            steps{
                sh './run_docker_tests.sh'
            }
        }
        stage('Pull Image'){
            steps{
                docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                    sh 'docker push nolram/django-template:latest'
                }
            }
        }
    }
}