pipeline{
    agent any
    stages{
        stage('Dev Test Env'){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh './script/install.sh'
                sh './script/make_service.sh'
                
                

            }
        }

    }
}