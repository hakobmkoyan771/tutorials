properties([parameters([choice(choices: ['1.16.5', '1.18.3', '1.17.11'], description: 'Golang version.', name: 'golang'), choice(choices: ['3.8.1-jdk-8', '3.8.6-openjdk-8-slim', '3.8.6-jdk-11'], description: 'Maven version.', name: 'maven')])])
podTemplate(containers: [
    containerTemplate(name: 'maven', image: "maven:${maven}", command: 'sleep', args: '99d'),
    containerTemplate(name: 'golang', image: "golang:${golang}", command: 'sleep', args: '99d')
  ]) {

    node(POD_LABEL) {
        stage('Get a Maven project') {
            git 'https://github.com/jenkinsci/kubernetes-plugin.git'
            container('maven') {
                stage('Build a Maven project') {
                    sh 'mvn -B -ntp clean install'
                }
            }
        }

        stage('Get a Golang project') {
            git url: 'https://github.com/hashicorp/terraform.git', branch: 'main'
            container('golang') {
                stage('Build a Go project') {
                    sh '''
                    mkdir -p /go/src/github.com/hashicorp
                    ln -s `pwd` /go/src/github.com/hashicorp/terraform
                    cd /go/src/github.com/hashicorp/terraform && make
                    '''
                }
            }
        }

    }
}
