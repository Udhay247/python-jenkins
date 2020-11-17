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
        stage('SCM') {
            steps {
                git url: 'https://github.com/Udhay247/python-jenkins.git'
            }
        }
        stage('build && SonarQube analysis') {
            steps {
                def scannerHome = tool 'sonarscanner1';
                withSonarQubeEnv('sonarqube') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.properties"
                }
            }
        }
    }
}