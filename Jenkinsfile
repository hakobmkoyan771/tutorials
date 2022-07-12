pipeline {
    agent {
        kubernetes {
            yamlFile "kaniko.yaml"
        }
    }
    triggers {
        GenericTrigger(causeString: 'Generic Trigger',
                        genericVariables: [[key: 'repo', value: '$.repository.full_name'],
                                           [key: 'repo_link', value: '$.repository.clone_url'],
                                           [key: 'default_branch', value: '$.repository.default_branch'],
                                           [key: 'reponame', value: '$.repository.name']])
    }
    stages {
        stage('Build image of repo & push to registry') {
            steps {
                sh "echo ${repo_link}"
                container('kaniko') {
                    dir("${repo}") {
                        git url: "${repo_link}", branch: "${default_branch}"
                        sh """/kaniko/executor --context `pwd` --destination hakobmkoyan771/${reponame}:_${env.BUILD_NUMBER}"""
                    }
                }
            }
        }
        stage('Run pod of created image in previous stage') {
            agent {
                kubernetes {
                    yaml """
                        apiVersion: v1
                        kind: Pod
                        metadata:
                            name: ${repo}
                        spec:
                            containers:
                                - name: ${repo}
                                  image: hakobmkoyan771/app:_${repo_link}
                    """
                }
            }
            steps {
                container("${repo}") {
                    sh "sleep 99d"
                }
            }
        }
    }
}
