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
    stage('Run prediction') {
      steps {
        sh 'curl -X POST http://127.0.0.1:9191/classify'
      }
    }
    stage('Push to git'){
      steps{
        sh 'git status'
        sh 'git add .'
        sh 'git commit -m "classification results"'
        sh 'git remote add origin'
      }
    }
  }
  
}
