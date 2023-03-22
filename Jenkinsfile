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
        sh 'curl -X POST http://127.0.0.1:9191/classify -o prediction.csv'
      }
    }
    stage('Push to git'){
      steps{
        sh 'git add .'
        sh 'commit -am.'
        sh 'git checkout -b master'
        sh 'push origin master'
      }
    }
  }
  
}
