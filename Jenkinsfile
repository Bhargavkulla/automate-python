pipeline {
    agent any

    stages {
        // Stage 1: Clone Repository
        stage('Clone Repository') {
            steps {
                // Pull code from GitHub
                git branch: 'main', url: 'https://github.com/your-repo/python-app.git'
            }
        }

        // Stage 2: Install Dependencies
        stage('Install Dependencies') {
            steps {
                // Install dependencies using pip
                sh 'pip install -r requirements.txt'
            }
        }

        // Stage 3: Run Tests
        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh 'pytest tests/'
            }
        }

        // Stage 4: Deploy to Staging
        stage('Deploy to Staging') {
            steps {
                // Deploy using SSH
                sshagent(['server-credentials']) {
                    sh 'scp -r * user@staging-server:/var/www/python-app'
                }
            }
        }
    }
}
