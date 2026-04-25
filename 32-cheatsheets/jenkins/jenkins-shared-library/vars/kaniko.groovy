def build() {
    try {
        def dockerBuild = """
            /kaniko/executor \
            --dockerfile="${WORKSPACE}/Dockerfile" \
            --context `pwd` \
            --tarPath="${WORKSPACE}/${BUILD_NUMBER}.tar" \
            --no-push
        """

        def exitCode = sh(script: dockerBuild, returnStatus: true)

        if (exitCode != 0) {
            error "Kaniko build failed with exit code: ${exitCode}"
        } else {
            echo "Kaniko build succeeded."
        }
    } catch (Exception e) {
        error "Exception during Kaniko build: ${e.getMessage()}"
    }
}

def push(String registryName, String imageTag, String registryCred) {
    withCredentials([usernamePassword(credentialsId: registryCred, usernameVariable: 'DOCKER_HUB_USR', passwordVariable: 'DOCKER_HUB_PSW')]) {
        script {
            try {
                sh """
                    echo '{"auths":{"https://index.docker.io/v1/":{"auth":"'"\$(echo -n ${DOCKER_HUB_USR}:${DOCKER_HUB_PSW} | base64)"'"}}}' > /kaniko/.docker/config.json
                    /kaniko/executor --dockerfile="/Dockerfile" --context "." --destination "${registryName}:${imageTag}"
                """
            } catch (Exception e) {
                echo "Error occurred during Kaniko build and push: ${e.getMessage()}"
                currentBuild.result = 'FAILURE'
                throw e
            }
        }
    }
}



