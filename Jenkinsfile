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
