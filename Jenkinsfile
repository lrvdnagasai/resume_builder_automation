pipeline {
    agent any

    parameters {
        choice(name: 'browser', choices: ['chrome', 'firefox'])
        choice(name: 'TEST_SCOPE', choices: ['all', 'smoke', 'regression', 'sanity'])
        booleanParam(name: 'HEADLESS_MODE', defaultValue: true)
        string(name: 'TEST_FILE', defaultValue: 'all', description: 'Test file to run')
    }

    stages {
        stage('Run Tests') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'pika-login-creds',
                    usernameVariable: 'PIKA_EMAIL',
                    passwordVariable: 'PIKA_PASSWORD'
                )]) {
                    sh '''
                        export JAVA_HOME=/Library/Java/JavaVirtualMachines/temurin-21.jdk/Contents/Home
                        export PATH=$JAVA_HOME/bin:$PATH

                        python3 -m venv venv
                        source venv/bin/activate

                        pip install --upgrade pip
                        pip install -r requirements.txt
                        playwright install

                        rm -rf allure-results
                        mkdir -p allure-results

                        # Verify credentials are present before running tests
                        echo "Email variable is set: $([ -n "$PIKA_EMAIL" ] && echo YES || echo NO)"
                        echo "Password variable is set: $([ -n "$PIKA_PASSWORD" ] && echo YES || echo NO)"

                        HEADLESS_FLAG=""
                        if [ "$HEADLESS_MODE" = "true" ]; then
                          HEADLESS_FLAG="--headless"
                        fi

                        FILE_FLAG=""
                        if [ -n "$TEST_FILE" ] && [ "$TEST_FILE" != "all" ]; then
                          FILE_FLAG="$TEST_FILE"
                        fi

                        if [ "$TEST_SCOPE" = "all" ]; then
                          pytest --browser_name "$browser" $HEADLESS_FLAG $FILE_FLAG -v -s --alluredir=allure-results
                        else
                          pytest --browser_name "$browser" -m "$TEST_SCOPE" $HEADLESS_FLAG $FILE_FLAG -v -s --alluredir=allure-results
                        fi
                    '''
                }
            }
        }
    }

    post {
        always {
            script {
                step([
                    $class: 'AllureReportPublisher',
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}