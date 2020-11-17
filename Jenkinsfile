node {
  stage('SCM') {
    git 'https://github.com/Udhay247/python-jenkins.git'
  }
  stage('SonarQube analysis') {
    def scannerHome = tool 'sonarscanner1';
    withSonarQubeEnv('sonarqube') { // If you have configured more than one global server connection, you can specify its name
      sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.properties"
    }
  }
}