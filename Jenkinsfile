node('ecs2') {ansiColor('xterm'){
  stage('Checkout') {
    scm checkout
  }

  stage('Test') {
    sh('python3 -m pytest')
    sh('python3 -m coverage erase')
    sh('python3 -m coverage run Calculator.py --branch')
    sh('python3 -m coverage xml -i')
  }

  stage('Sonar Analysis') {
    //Perform Sonar Analysis
  }

  stage('Archive Artifact') {
    //Push artifact to repository
  }
}}