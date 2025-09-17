pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'windows',
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
                    python -m pytest -s test/ --html=report.html --self-contained-html
                    echo ===== Tests Completed =====
                """
            }
        }

        stage('Archive Results') {
            steps {
                // Archive report.html from the workspace root
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
