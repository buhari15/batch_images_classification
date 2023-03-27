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
        sh ' nohup python3 -c "classify.py 2>&1 &" && sleep 4 '
      }
  }
  stage('Run Prediction') {
            steps {
                sh 'curl -X POST http://127.0.0.1:2121/classify'
            }
        }
   
}
}
