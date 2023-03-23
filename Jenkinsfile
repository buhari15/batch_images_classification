pipeline {
  agent any
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
    stage('Start Flask app') {
      steps {
        sh 'python3 classify.py &'
        
        

      }
    }
    stage('Run curl') {
      steps {
        
        sh 'curl http://127.0.0.1:5000/classify'
        

      }
    }
 
    
  }
  
}
