// node {
//   stage('SCM') {
//     git 'https://github.com/Udhay247/python-jenkins.git'
//   }
//   stage('SonarQube analysis') {
//     def scannerHome = tool 'sonarscanner1';
//     withSonarQubeEnv('sonarqube') { // If you have configured more than one global server connection, you can specify its name
//       sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.properties"
//     }
//   }
// }

pipeline {
    agent any
    stages {
        stage('build && SonarQube analysis') {
            environment {
                scannerHome = tool 'sonarscanner1'
            }
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh "coverage run -m pytest"
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.properties"
                }
            }
        }

        stage(' Quality Gate') {
            steps{
                timeout(time: 15, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}