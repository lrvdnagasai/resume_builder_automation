import pytest

from conftest import browserInstance
from page.login_page import LoginPage

# (keep your existing fixtures exactly as they are)

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "expected_result(text): expected result message printed when the test passes",
    )




@pytest.mark.smoke
@pytest.mark.expected_result("TC01: User lands on dashboard")
def test_login_valid_user(browserInstance, credentials):
    user = credentials["valid_user"]
    login = LoginPage(browserInstance)

    login.navigate()
    login.login_valid(user["email"], user["password"])


@pytest.mark.expected_result("TC02: Email validation error shown")
def test_login_invalid_email(browserInstance, credentials):
    user = credentials["invalid_email"]
    login = LoginPage(browserInstance)

    login.navigate()
    login.assert_invalid_email_format(user["email"])


@pytest.mark.expected_result("TC03: Password error shown")
def test_login_invalid_password(browserInstance, credentials):
    user = credentials["invalid_password"]
    login = LoginPage(browserInstance)

    login.navigate()
    login.assert_invalid_password(user["email"], user["password"])


@pytest.mark.expected_result("TC04: Email required validation")
def test_login_empty_email(browserInstance, credentials):
    login = LoginPage(browserInstance)

    login.navigate()
    login.assert_email_required()


@pytest.mark.expected_result("TC05: Password required validation")
def test_login_empty_password(browserInstance, credentials):
    user = credentials["valid_user"]
    login = LoginPage(browserInstance)

    login.navigate()
    login.assert_password_required(user["email"])

def test_about_us_navigation(browserInstance):
    login = LoginPage(browserInstance)
    login.navigate()
    login.about_us_navigation()

def test_terms_of_service_navigation(browserInstance):
    login = LoginPage(browserInstance)
    login.navigate()
    login.click_terms_of_service()

def test_privacy_policy_navigation(browserInstance):
    login = LoginPage(browserInstance)
    login.navigate()
    login.click_privacy_policy()

def test_home_page_navigation(browserInstance):
    login = LoginPage(browserInstance)
    login.navigate()
    login.home_page_navigation()

