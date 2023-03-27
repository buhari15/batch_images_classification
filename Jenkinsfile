pipeline {
  agent any
  triggers{
    cron('0 10 * * *')
  }
  stages {
    stage('Installing requirements') {
      steps {
        sh 'python3 -m pip install --upgrade pip'
        sh 'python3 -m pip install -r requirements.txt'
      }
    }
   
    stage('Start Flask'){
      steps{
        sh 'BUILD_ID=dontKillMe python3 classify.py '
        
      }
  }
  stage('Run Prediction') {
            steps {
                sh 'curl -X POST http://127.0.0.1:2121/classify'
            }
        }
   
}
}
