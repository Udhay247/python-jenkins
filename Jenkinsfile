node{
    checkout scm
    stage('Build') {
        def customImage = docker.build("pyjenkins:0.1", "--build-arg service='pyjenkins' --build-arg version=0.1 -f ./Dockerfile .")
    }
}