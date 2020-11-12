node{
    checkout scm
    stage('Build') {
      docker {
        docker.build("pyjenkins:0.1", "--build-arg service='pyjenkins' --build-arg version=0.1 -f ./Dockerfile .")
      }
    }
}