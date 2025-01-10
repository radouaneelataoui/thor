pipeline {
  agent any
  stages {
    stage('BUILD') {
      steps {
             fred_test
        echo 'Hello BUILD par fred'
      }
    }
    stage('TEST') {
      steps {
        echo 'Hello TEST par fred'
      }
    }
    stage('DEPLOY') {
      steps {
        echo ' DEPLOY par fred'
      }
    }
  }
}
