pipeline {
    agent {
        node {
            label ""
        }
    }
    stages {
        stage("clone repo") {
            steps {
                script {
                    sh """
                        echo "clone repo"
                    """
                }
            }
        }
        stage("build") {
            steps {
                script {
                    sh """
                        echo "build"
                    """
                }
            }
        }
        stage("test") {
            steps {
                script {
                    sh """
                        echo "test"
                    """
                }
            }
        }
        stage("deploy") {
            steps {
                script {
                    sh """
                        echo "deploy"
                    """
                }
            }
        }
    }
}
