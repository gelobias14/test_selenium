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

        stage('Run Tests') {
            steps {
                bat """
                    echo ===== Running Selenium Tests =====
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                    python test/test_google.py
                    echo ===== Tests Completed =====
                """
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'test/report.html', fingerprint: true
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
