@Library('jenkins-shared-library@master') _

pipeline {
    agent {
        kubernetes {
            yaml '''
                apiVersion: v1
                kind: Pod
                spec:
                  containers:
                  - name: maven
                    image: maven:3.8.4-openjdk-17
                    command:
                    - cat
                    tty: true
            '''
        }
    } 

    stages {
        stage('Checkout') {
            steps {
                gitCheckout(
                    url: 'https://github.com/spring-projects/spring-petclinic.git',
                    branch: 'main'
                )
            }
        }
        stage('Build') {
            steps {
                container('maven') {
                    script {
                        maven.build()
                    }
                }
            }
        }
    }
}

