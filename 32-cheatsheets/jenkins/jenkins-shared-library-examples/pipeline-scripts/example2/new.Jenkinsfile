pipeline {
    agent {
        node {
            label ""
        }
    }
    stages {
        stage("Hello World") {
            steps {
                example2() // example2() uses the default parameter. you can also try: ``example2 "hi"`` or ``example2 "hello"`` 
            }
        }
    }
}
