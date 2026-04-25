pipeline {
    agent {
        node {
            label ""
        }
    }
    stages {
        stage("Say Hello") {
            steps {
                script {
                    sh """
                        echo "Hello Alice"
                    """
                }
                script {
                    sh """
                        echo "How are you doing?"
                    """
                }
                script {
                    sh """
                        echo "Bye"
                    """
                }
            }
        }
    }
}
