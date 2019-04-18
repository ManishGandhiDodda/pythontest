def workspace
node
{
    stage ('Checkout Code')
    {
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '0becc3d3-39fd-4d03-9209-eec1722f0586', url: 'git@github.com:ManishGandhiDodda/pythontest.git']]])
        workspace = pwd()
    }    
    stage ('Code Analysis')
    {
        build job: 'Code Analysis', parameters: [string(name: 'workspace', value: workspace)]
    }
    stage ('Code Compile')
    {
        build job: 'Code Compile', parameters: [string(name: 'workspace', value: workspace)]
    }
    stage ('Code Unit-test')
    {
        build job: 'Code Unit-test', parameters: [string(name: 'workspace', value: workspace)]
    }
    stage ('Package')
    {
        build job: 'Package', parameters: [string(name: 'workspace', value: workspace)]
    }
    stage ('Deploy')
    {
        build job: 'Deploy', parameters: [string(name: 'workspace', value: workspace)]
    }
}
