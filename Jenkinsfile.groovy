pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from Bitbucket
                git branch: 'main',
                    url: 'https://bitbucket.org/your-team/your-repo.git',
                    credentialsId: 'bitbucket-creds'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/ --html=report.html --self-contained-html'
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
                junit 'tests/*.xml' // if you use --junitxml in pytest
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
