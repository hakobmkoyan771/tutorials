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
    triggers {
        GenericTrigger(causeString: 'Generic Trigger',
                        genericVariables: [[key: 'reponame', value: '$.repository.full_name'],
                                           [key: 'repo_link', value: '$.repository.git_url'],
                                           [key: 'default_branch', value: '$.repository.default_branch']]
    )
    stages {
        stage("Build image of ${reponame} repo") {
            steps {
                container('kaniko') {
                    dir("${reponame}") {
                        git url: "${repo_link}", branch: "${default_branch}"
                        sh "/kaniko/executor --context `pwd` --destination hakobmkoyan771/app:_${repo_link}${env.BUILD_NUMBER}"
                    }
                }
            }
        }
    }
}