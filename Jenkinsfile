pipeline {
  agent any
  stages {
    stage('Detectar variables en plantilla') {
      steps {
        script {
          // Leer la plantilla
          def tpl = readFile file: 'scp-template.json.tpl'

          // Buscar todas las variables del tipo ${var}
          def matcher = tpl =~ /\${([A-Za-z0-9_]+)}/
          def variables = matcher.collect { it[1] }.unique()

          // Construir parámetros dinámicos
          def inputs = variables.collect { varName ->
            return string(name: varName, description: "Ingresa valor para ${varName}")
          }

          // Solicitar los valores al usuario
          def values = input message: 'Variables requeridas para el SCP:', parameters: inputs

          // Exportar como TF_VAR_ para que Terraform los use
          values.each { k, v ->
            env."TF_VAR_${k}" = v
          }
        }
      }
    }

    stage('Terraform Init & Apply') {
      steps {
        sh 'terraform init'
        sh 'terraform apply -auto-approve'
      }
    }
  }
}
