pipeline {
  agent any

  stages {
    stage('Detectar variables (Python)') {
      steps {
        script {
          // Ejecuta el script para detectar variables, imprime JSON plano: ["VAR1", "VAR2", ...]
          def raw = sh(script: "python3 extract_vars.py", returnStdout: true).trim()

          // Parsea el output como lista
          def variables = readJSON text: raw

          if (variables.size() == 0) {
            echo "No se detectaron variables de entorno en la SCP."
          } else {
            // Genera la lista de parámetros de entrada
            def inputs = variables.collect { varName ->
              return string(name: varName, description: "Valor para ${varName}")
            }

            // Muestra input interactivo para el usuario
            def values = input message: 'Ingresa valores para las variables del SCP', parameters: inputs

            // Exporta como variables de entorno tipo TF_VAR_ para Terraform
            values.each { k, v ->
              env."TF_VAR_${k}" = v
            }

            // Vuelve a ejecutar el script con las variables seteadas, ahora para generar terraform.auto.tfvars.json
            sh 'python3 extract_vars.py'
          }
        }
      }
    }

    stage('Terraform Plan') {
            steps {
                script {
                    // Genera el plan de Terraform
                    sh 'terraform init'
                    sh 'terraform plan -out=tfplan'
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                input message: '¿Estás seguro de que deseas aplicar el plan?', ok: 'Sí'
                script {
                    // Aplica el plan de Terraform
                    sh 'terraform apply tfplan'
                }
            }
        }
  }
}
