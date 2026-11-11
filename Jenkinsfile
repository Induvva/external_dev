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
                echo 'Running tests...'
                bat "docker run -p 5000:5000 pythonapp:register"
            }
        }
        
    }
    post{
        success{
            echo 'Pipeline completed successfully.'
        }
        fialure{
            echo 'Pipeline failed.'
        }
    }
}