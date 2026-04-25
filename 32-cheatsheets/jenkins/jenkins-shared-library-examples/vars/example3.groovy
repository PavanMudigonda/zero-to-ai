def call(Closure postHelloScript) {
    node {
        stage("Hello World") {
            script {
                sh """
                    echo Hello
                """
            }
        }
        postHelloScript()
    }
}

