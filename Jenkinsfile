pipeline {
    agent any

    stages {
        // Stage 1: Clone Repository
        stage('Clone Repository') {
            steps {
                // Pull code from GitHub
                git branch: 'main', url: 'https://github.com/Bhargavkulla/automate-python.git'
            }
        }

        // Stage 2: Install Dependencies
        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    // Activate virtual environment and install dependencies
                    sh '''
                        source venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        // Stage 3: Run Tests
        stage('Run Tests') {
            steps {
                script {
                    // Activate virtual environment and run tests
                    sh '''
                        source venv/bin/activate
                        pytest tests/
                    '''
                }
            }
        }

        // Stage 4: Deploy to Staging (Public SSH Key Authentication)
        stage('Deploy to Staging') {
            steps {
                script {
                    // Assuming the SSH private key is stored on the Jenkins agent and the public key is on the server
                    // Set up the SSH private key path
                    def sshKeyPath = '/path/to/your/private/key'

                    // Deploy using SCP with public SSH key authentication
                    sh """
                        chmod 600 ${sshKeyPath}  # Ensure correct file permissions for the SSH key
                        scp -i ${sshKeyPath} -r * user@staging-server:/var/www/python-app
                    """
                }
            }
        }
    }
}
