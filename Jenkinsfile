node{
    checkout scm
    stage('Build') {
      docker.withRegistry('http://nexus.cicd.sv2.247-inc.net:5000', 'nexus-admin') {
        docker.build("pyjenkins:0.1", "--build-arg service='pyjenkins' --build-arg version=0.1 -f ./Dockerfile .")
      }
    }
}