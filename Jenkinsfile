pipeline {
    agent any
    stages {
        stage("Code coverage"){
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

        stage('Coverage report'){
            steps{
                sh "docker run -v \$(pwd)/target:/mnt/app/ --rm pythonenv cp coverage.xml /mnt/app/"
            }
        }
        stage('SonarQube analysis') {
            environment {
                scannerHome = tool 'sonarscanner1'
            }
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.properties"
                }
            }
        }

        stage('Quality Gate') {
            steps{
                timeout(time: 2, unit: 'MINUTES') {
                    script{
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                          error "Sonar quality gate status: ${qg.status}"
                        }
                    }
                }
            }
        }

        stage('Nexus deploy'){
            steps{
                docker.withRegistry('http://nexus.cicd.sv2.247-inc.net:5000', 'nexus-admin') {
                    docker.build("pyjenkins:1.3", "--build-arg service='pyjenkins' --build-arg version=1.3 -f ./Dockerfile_nexus_push .")
                    //customImage.push()
                }
            }
        }
    }
}