def call(String directory) {
      script {
         def tflintCommand = "tflint --chdir=${directory}"

         def tflintOutput = sh(script: tflintCommand, returnStatus: true)

         echo "Tflint Exit Code: ${tflintOutput}"

         if (tflintOutput != 0) {
               error "Tflint failed with exit code ${tflintOutput}"
         }
      }
}

