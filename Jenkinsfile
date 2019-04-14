pipeline {
  agent {
    docker {
      image '83b205d8021c195ea1ff86a66dce1d12ed398d17'
      args '--privileged -p 9090:8000 -p 8089:8089'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Build'
        sh 'python /work/toDoListPro/manage.py runserver 0.0.0.0:8000'
      }
    }
    stage('Test') {
      parallel {
        stage('Functional Test') {
          steps {
            echo 'Executing Functional Test'
            sh 'python chapter5/DjangoTest/tests/testDjangoTodo_1.py'
          }
        }
        stage('Performance Test') {
          steps {
            echo 'Executing performance test'
            sh 'locust -H http://127.0.0.1:8000 --no-web -t 100 -c 100 -r 20  -f chapter5/PerformanceTest/djangoperftest'
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploy'
      }
    }
  }
}