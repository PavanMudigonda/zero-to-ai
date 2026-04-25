pipeline {
    agent {
        node {
            label ""
        }
    }
    stages {
        stage("Hello World") {
            steps {
                example6()
                script {
                    sh """
                        echo "fullname is"
                    """
                }
            }
        }
    }   
}
