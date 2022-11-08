pipeline {
    agent any

    environment {
        DEMO_SERVER = 'staging.sse.uni-hildesheim.de'
        DEMO_SERVER_USER = "elscha"
        REMOTE_UPDATE_SCRIPT = '/staging/update-compose-project.sh nm-competence-repository'
    }

    stages {

        stage('Git') {
            steps {
                cleanWs()
                git branch: 'main', url: 'https://github.com/e-Learning-by-SSE/nm-competence-ai-service.git'
            }
        }
        
        stage('Check') {
            steps {
                sh 'python3 -m py_compile */*.py'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Based on:
                    // - https://e.printstacktrace.blog/jenkins-pipeline-environment-variables-the-definitive-guide/
                    // - https://stackoverflow.com/a/16817748
                    // - https://stackoverflow.com/a/51991389
                    env.API_VERSION = sh(returnStdout: true, script: 'grep -Po "(?<=app = flask_app, version=\')[^\']+" search_pi/findPath.py').trim()
                    echo "API: ${env.API_VERSION}"
                    dockerImage = docker.build 'e-learning-by-sse/nm-competence-ai-service'
                    docker.withRegistry('https://ghcr.io', 'github-ssejenkins') {
                        dockerImage.push("${env.API_VERSION}")
                        dockerImage.push('latest')
                    }
                }
            }
        }

        // Based on: https://medium.com/@mosheezderman/c51581cc783c
        stage('Deploy') {
            steps {
                sshagent(credentials: ['Stu-Mgmt_Demo-System']) {
                    sh "ssh -i ~/.ssh/id_rsa_student_mgmt_backend ${DEMO_SERVER_USER}@${env.DEMO_SERVER} ${REMOTE_UPDATE_SCRIPT}"
                }
            }
        }
    }
}
