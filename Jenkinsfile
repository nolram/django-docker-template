pipeline{
    agent any
    stages {
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
    }
}