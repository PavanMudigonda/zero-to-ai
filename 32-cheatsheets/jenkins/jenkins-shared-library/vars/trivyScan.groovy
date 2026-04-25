def kaniko() {
    script {
        def tplContent = libraryResource "org/dcube/trivy/html.tpl"
        writeFile file: "${WORKSPACE}/html.tpl", text: tplContent

        def trivyConfigContent = libraryResource "org/dcube/trivy/trivy.yml"
        writeFile file: "${WORKSPACE}/trivy.yml", text: trivyConfigContent

        def command = "trivy image --config ${WORKSPACE}/trivy.yml --template '@${WORKSPACE}/html.tpl' -o ${WORKSPACE}/trivy-report.html --input ${WORKSPACE}/${BUILD_NUMBER}.tar"

        def exitCode = sh(script: command, returnStatus: true)

        if (exitCode != 0) {
            error "Trivy scan found vulnerabilities"
        } else {
            echo "Trivy scan completed successfully with no critical vulnerabilities."
        }

        return exitCode
    }
}

def docker(String imageName, String imageTag) {
    try {
        setupTrivyFiles()

        def command = "trivy image --config ${WORKSPACE}/trivy.yml --template '@${WORKSPACE}/html.tpl' -o ${WORKSPACE}/trivy-report.html ${imageName}:${imageTag}"
        def result = runTrivyCommand(command)

        return result.exitCode
    } catch (Exception e) {
        error "Exception during Trivy scan for Docker image ${imageName}:${imageTag}: ${e.getMessage()}"
    }
}