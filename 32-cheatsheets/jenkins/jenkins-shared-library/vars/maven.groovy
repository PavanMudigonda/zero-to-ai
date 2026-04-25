def build() {
    def mvnCommand = 'mvn -B -Dmaven.repo.local=/root/.m2/repository clean install -DskipTests'
    def exitCode = sh(script: mvnCommand, returnStatus: true)

    if (exitCode != 0) {
        error "Maven build failed with exit code: $exitCode"
    }
}

def test() {
    def mvnCommand = 'mvn test'
    def exitCode = sh(script: mvnCommand, returnStatus: true)

    if (exitCode != 0) {
        error "Maven test failed with exit code: $exitCode"
    }
}