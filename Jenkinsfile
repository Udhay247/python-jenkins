pipeline{
    agent any

    stages{
        stage('SonarQube analysis') {
            steps {
                def scannerHome = tool 'sonarscanner1'
                withSonarQubeEnv('sonarqube'){
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.properties"
                }
            }
        }
    }

//     stage('Build') {
//         def customImage = docker.build("pyjenkins:0.1", "--build-arg service='pyjenkins' --build-arg version=0.1 -f ./Dockerfile .")
//     }
}