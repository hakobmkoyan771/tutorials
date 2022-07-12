pipeline {
    agent {
        kubernetes {
            yamlFile "kaniko.yaml"
        }
    }
    triggers {
        GenericTrigger(causeString: 'Generic Trigger',
                        genericVariables: [[key: 'reponame', value: '$.repository.full_name'],
                                           [key: 'repo_link', value: '$.repository.git_url'],
                                           [key: 'default_branch', value: '$.repository.default_branch']])
    }
    stages {
        stage('Build image of repo & push to registry') {
            steps {
                sh "echo ${repo_link}"
                container('kaniko') {
                    dir("${reponame}") {
                        git url: """${repo_link}, branch: 'main'"""
                        sh """/kaniko/executor --context `pwd` --destination hakobmkoyan771/app:_${repo_link}"""
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
                            name: ${reponame}
                        spec:
                            containers:
                                - name: ${reponame}
                                  image: hakobmkoyan771/app:_${repo_link}
                    """
                }
            }
            steps {
                container("${reponame}") {
                    sh "sleep 99d"
                }
            }
        }
    }
}
