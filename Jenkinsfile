pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                echo 'Building the Docker image...'
                bat "docker build -t pythonapp:register ."
            }
        }
        stage('Test'){
            steps{
                echo 'Running Flask tests...'
                bat "docker run --rm pythonapp:register python -m unittest discover -s tests -v"
            }
        }
        
    }
    post{
        success{
            echo 'Pipeline completed successfully.'
        }
        failure{
            echo 'Pipeline failed.'
        }
    }
}