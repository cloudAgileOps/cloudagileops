pipeline {
  agent {
    dockerfile {
      filename 'chapter4/Dockerfile'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Build'
        sh 'make'
      }
    }
    stage('Test') {
      parallel {
        stage('Functional Test') {
          steps {
            echo 'Executing Functional Test'
            sh 'python testFunctional.py'
          }
        }
        stage('Performance Test') {
          steps {
            echo 'Executing performance test'
            sh 'python testPerformance.py'
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploy'
        sh 'deploy'
      }
    }
  }
}