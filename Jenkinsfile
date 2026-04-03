pipeline {
    agent any

    parameters {
        choice(name: 'browser', choices: ['chrome', 'firefox'])
        choice(name: 'TEST_SCOPE', choices: ['all', 'smoke', 'regression', 'sanity'])
        booleanParam(name: 'HEADLESS_MODE', defaultValue: true)
        choice(
            name: 'TEST_FILE',
            choices: [
                'tests/',
                'tests/login/test_login.py',
                'tests/dashboard/test_dashboard.py',
                'tests/landing/test_landing_page.py',
                'tests/referral/test_referral.py'
            ],
            description: 'Select which test directory or file to run'
        )
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
                        playwright install chromium firefox

                        rm -rf allure-results
                        mkdir -p allure-results

                        # Verify credentials are present before running tests
                        echo "Email variable is set: $([ -n "$PIKA_EMAIL" ] && echo YES || echo NO)"
                        echo "Password variable is set: $([ -n "$PIKA_PASSWORD" ] && echo YES || echo NO)"

                        HEADLESS_FLAG=""
                        if [ "$HEADLESS_MODE" = "true" ]; then
                          HEADLESS_FLAG="--headless"
                        fi

                        TARGET_PATH="$TEST_FILE"

                        if [ "$TEST_SCOPE" = "all" ]; then
                          pytest "$TARGET_PATH" --browser_name "$browser" $HEADLESS_FLAG -v -s --alluredir=allure-results
                        else
                          pytest "$TARGET_PATH" --browser_name "$browser" -m "$TEST_SCOPE" $HEADLESS_FLAG -v -s --alluredir=allure-results
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