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
   stage('Compile all') {
      steps {
        sh 'python3 -m py_compile classify.py'
        echo 'All python code compiled'
      }
    }
    stage('Start Flask'){
      steps{
        sh 'python3 classify.py &'
        
      }
  }
    stage('Run Prediction') {
        steps{
          sh 'curl -X POST http://127.0.0.1:5000/classify'
        }
      }
    
    stage('Push to git'){
      steps{
        sh 'git add .'
        sh 'git commit -m "Updated"'
        sh 'git push origin master'
      }
    }
   
}
}
