node {
    stage('Clone repository') {
        checkout scm
    }

    stage('Build and Push ARM64 Image') {
        // Register QEMU emulation (safe to do every time)
        sh 'docker run --rm --privileged multiarch/qemu-user-static --reset -p yes'
        // Create and use a buildx builder (safe if builder exists)
        sh 'docker buildx create --name multiarch --use || true'
        // Build and push ARM64 image to Docker Hub
        sh """
            docker buildx build \
                --platform linux/arm64 \
                -t kartikj69/test:${env.BUILD_NUMBER} \
                --push .
        """
    }

    stage('Trigger ManifestUpdate') {
        echo "triggering updatemanifestjob"
        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
    }
}
