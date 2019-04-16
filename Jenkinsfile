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
                    sh 'pytest tests -s -n2 --junitxml=./reports/result1.xml'
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
