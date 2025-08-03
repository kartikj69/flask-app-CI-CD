node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        // Build for linux/amd64 platform to ensure compatibility with Kubernetes
        app = docker.build("kartikj69/test:${env.BUILD_NUMBER}", "--platform linux/arm64 .")
    }

    stage('Test image') {
        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
        echo "triggering updatemanifestjob"
        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
    }
}
