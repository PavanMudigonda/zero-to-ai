def call() {
    stage("clone repo") {
        steps {
            script {
                sh """
                    echo "clone repo"
                """
            }
        }
    }
}

