pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    }
    stages {
        stage('pre') {
            steps {
                sh 'pwd'
                sh 'python3 --version'
                sh 'pytest --version'
            }
        }
        stage('parallel automation') {
            steps {
                sauce('penny') {
                    sh 'pytest -s -n2 --junitxml=./reports/result1.xml'
                    sh 'cat $(find . -name "*.testlog")'
                }
            }
        }
    }
    post {
        always {
            junit 'reports/*.xml'
        }
    }
}
