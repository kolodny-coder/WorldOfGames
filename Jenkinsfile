pipeline {
  agent { label "linux" }
  stages {
    stage("build") {
      steps {
        sh """
          docker-compose build
        """
      }
    }
    stage("run") {
      steps {
        sh """
          docker-compose up
        """
      }
    }
  }
}