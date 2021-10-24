pipeline {
  agent { label "master" }
  stages {
    stage("build") {
      steps {
        sh """
          docker build .
        """
      }
    }
    stage("run") {
      steps {
        sh """
          docker run
        """
      }
    }
  }
}
