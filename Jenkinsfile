stage('Detectar variables (Python)') {
  steps {
    script {
      def raw = sh(script: "python3 extract_vars.py", returnStdout: true).trim()
      def variables = readJSON text: raw

      def inputs = variables.collect { varName ->
        return string(name: varName, description: "Valor para ${varName}")
      }

      def values = input message: 'Ingresa valores para el SCP', parameters: inputs

      // Setea como TF_VAR_xx para que Terraform los detecte
      values.each { k, v ->
        env."TF_VAR_${k}" = v
      }

      // Ejecutar de nuevo el script para generar terraform.auto.tfvars.json
      sh 'python3 extract_vars.py'
    }
  }
}
