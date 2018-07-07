pipeline {
    agent any
    stages {
        /*stage('Build') {
            steps {
                sh 'vagrant up --destroy-on-error'
                sh 'python build-templates.py'
            }
        } */
        stage('Test') {
            steps {
                sh 'python test-templates.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
    post {
        always {
            echo 'Destroying vagrant VMs...'
            sh 'vagrant destroy -f'
        }
        failure {
            sh 'python update-build-icon.py -f'
        }
    }
}