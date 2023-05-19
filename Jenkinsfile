pipeline {
  agent any
  triggers{
    cron('0 0 * * *')
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
        sh 'python3 -m py_compile code/classify.py'
        echo 'All python code compiled'
      }
    }
    stage('Start Flask'){
      steps{
        sh ' python3 code/classify.py & sleep 20'
       
        
      }
  }
    stage('Run Prediction') {
        steps{
          sh 'curl -X POST http://127.0.0.1:5000/classify'

          // Commit and push the classification results to GitHub
          // sh 'git config --global user.email "jenkins@example.com"'
          // sh 'git config --global user.name "Jenkins"'
          // sh 'git add classification.csv'
          // sh 'git commit -m "Add classification results"'
          // sh 'git push origin master' 
        }
      }
    
   
   
}
}
