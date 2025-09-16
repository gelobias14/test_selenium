pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/venv"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/gelobias14/test_selenium.git', 
                    credentialsId: 'GIT_CRED'
            }
        }

        stage('Setup Python') {
            steps {
                // Create virtual environment
                sh "python -m venv ${VENV}"

                // Activate and upgrade pip
                sh """
                    source ${VENV}/Scripts/activate
                    python -m pip install --upgrade pip
                """

                // Install dependencies
                sh """
                    source ${VENV}/Scripts/activate
                    pip install -r requirements.txt
                    pip install webdriver-manager
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    source ${VENV}/Scripts/activate
                    pytest test/ --html=report.html --self-contained-html
                """
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            echo "✅ Tests Passed!"
        }
        failure {
            echo "❌ Tests Failed! Check report.html for details."
        }
    }
}
