pipeline {
    agent any

    environment {
        IMAGE_NAME = 'healthcare-app'
        CONTAINER_NAME = 'healthcare-web'
        PORT = '8080'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'python3 test_app.py'
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    sh '''
                    if [ $(docker ps -q -f name=$CONTAINER_NAME) ]; then
                        docker stop $CONTAINER_NAME
                        docker rm $CONTAINER_NAME
                    fi
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh '''
                    docker run -d --name $CONTAINER_NAME -p $PORT:$PORT $IMAGE_NAME
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Healthcare app deployed successfully on port $PORT"
        }
        failure {
            echo "Build or deployment failed!"
        }
    }
}