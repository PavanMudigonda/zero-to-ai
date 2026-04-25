pipeline {
    agent {
        node {
            label ""
        }
    }
    stages {
        stage("Hello World") {
            steps {
                script {
                    sh """
                        echo Hello
                    """
                }
            }
        }
        stage("Post Hello") {
            steps {
                script {
                    sh """
                        echo post hello
                    """
                }
            }
        }
    }
}
