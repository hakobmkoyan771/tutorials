pipeline {
    agent none
    stages {
        stage('Build docker image and push to repository') {
            agent {
                kubernetes {
                    yaml '''
                    apiVersion: v1
                    kind: Pod
                    metadata:
                        name: kaniko
                    spec:
                        containers:
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
            steps { 
                container('kaniko') {
                    sh 'ls'
                }
            }
        }
    }
}
