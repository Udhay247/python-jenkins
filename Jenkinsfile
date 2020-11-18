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
        stage("Generating coverage"){
            agent{
                dockerfile{
                    filename 'Dockerfile'
                    additionalBuildArgs '-t pythonenv'
                }
            }
            steps{
                sh "coverage run -m pytest && coverage report && coverage xml"
            }
        }

//         stage('Copying coverage report from container'){
//             steps{
//                 sh " docker cp pythonenv:/app/python-services/coverage.xml ."
//             }
//         }
        stage('build && SonarQube analysis') {
            environment {
                scannerHome = tool 'sonarscanner1'
            }
            steps {
                withSonarQubeEnv('sonarqube') {
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