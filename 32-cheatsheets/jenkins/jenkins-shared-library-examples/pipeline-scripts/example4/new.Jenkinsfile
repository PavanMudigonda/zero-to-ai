pipeline {
    agent {
        node {
            label ""
        }
    }
    stages {
        stage("Say Hello") {
            steps {
                example4()
                script {
                    sh """
                        echo "Bye"
                    """
                }
            }
        }
    }
}
