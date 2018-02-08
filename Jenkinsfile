pipeline{
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    stages {
        // stage('Clone repository') {
        //     steps{
        //         checkout scm
        //     }
        // }
        stage('Build'){
            steps{
                sh 'git archive -o django-template.tar HEAD'
                sh 'docker build -t nolram/django-template:latest -f Dockerfile.prod .'
            }
        }
        stage('Sonar'){
            steps{
                script {
                    // requires SonarQube Scanner 2.8+
                    scannerHome = tool 'SonarQube Scanner'
                }
                withSonarQubeEnv("SonarQube"){
                    sh "${scannerHome}/bin/sonar-scanner  -Dsonar.projectKey=django-template -Dsonar.sources=."
                }
            }
        }
        stage('Test'){
            steps{
                sh './run_docker_tests.sh'
            }
        }
        stage('Pull Image'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'docker-marlon-registry', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                    sh 'docker push nolram/django-template:latest'
                }
            }
        }
    }
}