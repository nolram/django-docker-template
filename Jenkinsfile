pipeline{
    agent any
    stages {
        stage('Build'){
            steps{
                sh 'echo hello world idjslfkjas'
                sh 'docker build nolram/django-template:latest --rm -f Dockerfile.prod .'
            }
        }
    }
}