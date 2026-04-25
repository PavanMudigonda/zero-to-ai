def call(String reportPath, String recipient) {
    script {
        def tplContent = libraryResource "org/dcube/notification/notify.tpl"

        def buildStatus = currentBuild.currentResult
        def statusColor = buildStatus == 'SUCCESS' ? 'green' : 'red'
        def headerColor = buildStatus == 'SUCCESS' ? '#28a745' : '#dc3545'

        tplContent = tplContent.replace('${BUILD_STATUS}', buildStatus)
                               .replace('${STATUS_COLOR}', statusColor)
                               .replace('${HEADER_COLOR}', headerColor)

        writeFile file: "${WORKSPACE}/notify.tpl", text: tplContent
    }

    def emailParams = [
        subject: "${JOB_NAME} - Build #${BUILD_NUMBER} - ${currentBuild.currentResult}",
        body: readFile("${WORKSPACE}/notify.tpl"),
        to: recipient,
        mimeType: 'text/html'
    ]

    if (currentBuild.currentResult != 'SUCCESS') {
        emailParams['attachmentsPattern'] = reportPath
    }

    emailext emailParams
}
