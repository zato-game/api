pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                sh "virtualenv python"
                sh "python/bin/pip install flask"
                sh "python/bin/pip install flask-mysqldb"
            }
        }
        stage("Dev-deploy") {
            steps {
                echo "Deploying to development.."
            }
        }
        stage("Prod-Deploy") {
            steps {
                echo 'Deploying to production....'
            }
        }
    }
}
