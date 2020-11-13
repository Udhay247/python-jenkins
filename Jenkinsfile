pipeline{
    agent any

    stages{
        stage('SonarQube analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh "./gradlew sonarqube"
                }
            }
        }
        stage("Quality gate") {
            steps {
                waitForQualityGate abortPipeline: true
            }
        }
    }

//     stage('Build') {
//         def customImage = docker.build("pyjenkins:0.1", "--build-arg service='pyjenkins' --build-arg version=0.1 -f ./Dockerfile .")
//     }
}