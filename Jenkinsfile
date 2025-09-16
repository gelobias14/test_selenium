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

                // Upgrade pip using venv Python directly
                sh './venv/bin/python -m pip install --upgrade pip || venv\\Scripts\\python -m pip install --upgrade pip'

                // Install requirements using venv Python
                sh './venv/bin/python -m pip install -r requirements.txt || venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using venv Python directly
                sh './venv/bin/python -m pytest test/ --html=report.html --self-contained-html || venv\\Scripts\\python -m pytest test/ --html=report.html --self-contained-html'
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
