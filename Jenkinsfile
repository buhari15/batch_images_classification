pipeline {
  agent any
  stages {
    stage('Installing requirements') {
      steps {
        sh 'python3 -m pip install --upgrade pip'
        sh 'python3 -m pip install -r requirements.txt'
      }
    }
   
    
    stage('Start Flask'){
      steps{
        sh 'python3 classify.py '
      }

    }
   
 
    
  }
  
}
