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
        sh 'python3 -m py_compile prediction.py'
        echo 'All python code compiled'
      }
    }
    stage('Start Flask app') {
      steps {
        sh 'python3 prediction.py &'

      }
    }
    stage('Run prediction') {
      steps {
        sh 'curl -X POST http://127.0.0.1:9079/classify'
      }
    }
  }
}
