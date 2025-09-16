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
                bat 'run_tests.bat'
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
