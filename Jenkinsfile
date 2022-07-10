pipeline {
    agent {
        kubernetes {
            yaml '''
            apiVersion: v1
            kind: Pod
            metadata:
                name: kaniko
            spec:
                containers:
                    - name: ubuntu
                      image: ubuntu
                      command:
                      - sleep
                      args:
                      - 9999999
                    - name: kaniko
                      image: gcr.io/kaniko-project/executor:debug
                      command:
                      - sleep
                      args:
                      - 9999999
                      volumeMounts:
                        - name: docker-cred
                          mountPath: /kaniko/.docker
                volumes:
                    - name: docker-cred
                      secret:
                        secretName: dockercred
                        items:
                          - key: .dockerconfigjson
                            path: config.json
            '''
        }
    }
    stages {
        stage('Build image of hakobmkoyan771/jenkinskubernetes repo') {
            steps {
                sh 'whoami, hostname'
                container('kaniko') {
                    sh 'ls /'
                    git url: "https://github.com/hakobmkoyan771/jenkinskubernetes.git", branch: "main"
                    sh "/kaniko/executor --context `pwd` --destination hakobmkoyan771/app:_${env.BUILD_NUMBER}"
                }
            }
        }
        stage('Build image of hashicorp/terraform repo') {
            steps {
                container('kaniko') {
                    git url: "https://github.com/hashicorp/terraform.git", branch: "main"
                }
            }
        }
    }
}
