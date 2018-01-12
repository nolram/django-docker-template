pipeline{
    agent any
    steps{
        step('Build'){
            sh 'docker build nolram/django-template:latest --rm -f Dockerfile.prod .'
        }
    }
}