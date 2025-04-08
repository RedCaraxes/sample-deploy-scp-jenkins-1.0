pipeline {
    agent any
    
    environment {
        AWS_REGION = 'us-east-1'  // Cambia esta región si es necesario
        TF_VAR_my_var = 'my_value'  // Variables de entorno si es necesario para Terraform
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/tu_usuario/tu_repositorio.git'
            }
        }

        stage('Terraform Init') {
            steps {
                script {
                    // Inicializa Terraform
                    sh 'terraform init'
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                script {
                    // Genera el plan de Terraform
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

    post {
        success {
            echo 'Pipeline ejecutado con éxito.'
        }
        failure {
            echo 'La ejecución del pipeline falló.'
        }
    }
}
