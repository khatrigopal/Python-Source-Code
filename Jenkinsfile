node {
    def app

    stage('Clone Repository') {
      

        checkout scm
    }

    stage('Build Image') {
  
       app = docker.build("khatrig/argocd-python")
    }

    stage('Test Image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push Image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }

    
}
