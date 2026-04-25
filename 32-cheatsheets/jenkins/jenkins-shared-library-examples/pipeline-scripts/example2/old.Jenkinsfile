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
                        echo Hi Alice
                    """
                }
            }
        }
    }
}
