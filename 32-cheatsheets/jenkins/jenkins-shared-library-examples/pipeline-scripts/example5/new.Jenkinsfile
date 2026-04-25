pipeline {
    agent {
        node {
            label ""
        }
    }
    stages {
        example5()
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
