def call(String firstname="Obama", String lastname="Barrack") {
    script {
        sh """
            echo Hi Alice
        """
    }
    return "Yes Man"
}
