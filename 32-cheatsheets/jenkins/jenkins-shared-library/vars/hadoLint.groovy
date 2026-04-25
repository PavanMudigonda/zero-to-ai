def call() {
    
    script {
                    def tplContent = libraryResource "org/dcube/hadolint/.hadolint.yaml"
                    writeFile file: "${WORKSPACE}/.hadolint.yaml", text: tplContent
                }

    def hadolintCommand = "hadolint --config ${WORKSPACE}/.hadolint.yaml ${WORKSPACE}/Dockerfile"

    def hadolintOutput = sh(script: hadolintCommand, returnStatus: true)

    echo "Hadolint Exit Code: ${hadolintOutput}"

    if (hadolintOutput != 0) {
        error "Hadolint failed with exit code ${hadolintOutput}"
    }
}
