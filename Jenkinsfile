pipeline{
    agent any
    stages{
        stage('Dev Test Env'){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                
                sh './script/make_service.sh'
                
                sh '/var/lib/jenkins/workspace/pipeline1/venv/bin/coverage run -m /var/lib/jenkins/workspace/pipeline1/testing.py'
                sh '/var/lib/jenkins/workspace/pipeline1/venv/bin/coverage report -m'
                
                

            }
        }

    }
}