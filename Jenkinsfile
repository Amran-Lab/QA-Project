pipeline{
    agent any
    stages{
        stage('Dev Test Env'){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                
                sh './script/make_service.sh'
                
                sh 'coverage run -m pytest testing.py'
                sh 'coverage report -m'
                
                

            }
        }

    }
}