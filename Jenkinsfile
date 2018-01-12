pipeline{
    agent any
    steps{
        step('Build'){
            sh "echo 'hello world'"
            sh 'docker build nolram/django-template:latest --rm -f Dockerfile.prod .'
        }
    }
}