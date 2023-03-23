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
    stage('Activate virtual environment') {
      steps {
        sh 'http://localhost:8080/job/model_to_production/106/execution/node/3/ws/activate_venv.sh'
        
        echo 'Virtual environment activated'
        
      }
    }
   
 
    
  }
  
}
