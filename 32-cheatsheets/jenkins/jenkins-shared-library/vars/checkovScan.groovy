def call(String directory) {
    
    script {
                    def tplContent = libraryResource "org/dcube/checkov/.checkov.yaml"
                    writeFile file: "${WORKSPACE}/.checkov.yaml", text: tplContent
                }

    def checkovCommand = "checkov --directory ${directory} --config-file ${WORKSPACE}/.checkov.yaml"

    def checkovOutput = sh(script: checkovCommand, returnStatus: true)

    echo "checkov Exit Code: ${checkovOutput}"

    if (checkovOutput != 0) {
        error "checkov failed with exit code ${checkovOutput}"
    }
}