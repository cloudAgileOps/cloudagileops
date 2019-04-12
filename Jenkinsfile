pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build'
        sh 'sh \'make\''
      }
    }
    stage('Test') {
      parallel {
        stage('Functional Test') {
          steps {
            echo 'Functional Test'
            sh 'python testFunction.py'
          }
        }
        stage('Performance Test') {
          steps {
            echo 'Performance Test'
            sh 'python testPerformance.py'
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploy'
        sh '''cd $PROD_LANDSCAPE_DIR 
sh \'deploy\''''
      }
    }
  }
  environment {
    PROD_LANDSCAPE_DIR = '/prod/env/'
  }
}