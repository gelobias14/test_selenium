pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/gelobias14/test_selenium.git',
                    credentialsId: 'GIT_CRED'
            }
        }

        stage('Setup Python') {
            steps {
                // Create virtual environment
                sh 'python -m venv venv'

                // Use Windows-style path for venv Python
                sh 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                sh 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests with venv Python
                sh 'venv\\Scripts\\python.exe -m pytest test/ --html=report.html --self-contained-html'
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }

    post {
        success {
            echo '✅ Tests Passed!'
        }
        failure {
            echo '❌ Tests Failed! Check report.html for details.'
        }
    }
}
