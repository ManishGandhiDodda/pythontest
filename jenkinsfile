def workspace;
node
{
    stage('checkout')
    {
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '0becc3d3-39fd-4d03-9209-eec1722f0586', url: 'git@github.com:ManishGandhiDodda/pythontest.git']]])
        workspace = pwd()
    }
    stage('Build')
    {
        echo "Build Stage"
    }
    stage('Code Analysis')
    {
        echo "Code Analysis stage"
    }
    stage('Deploy')
    {
        echo "Deployement stage"
    }
}
