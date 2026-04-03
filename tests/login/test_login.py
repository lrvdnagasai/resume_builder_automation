import allure
import pytest

from page.login.login_page import LoginPage


@allure.feature("Login")
@allure.story("Valid Login")
@pytest.mark.smoke
@pytest.mark.expected_result("TC01: User lands on dashboard")
def test_login_valid_user(browserInstance, credentials):
    user = credentials["valid_user"]
    login = LoginPage(browserInstance)

    login.navigate()
    login.login_valid(user["email"], user["password"])


@allure.feature("Login")
@allure.story("Invalid email Login")
@pytest.mark.smoke
def test_login_invalid_email(browserInstance, credentials):
    user = credentials["invalid_email"]
    login = LoginPage(browserInstance)

    login.navigate()
    login.assert_invalid_email_format(user["email"])


@allure.feature("Login")
@allure.story("Invalid Password Login")
@pytest.mark.expected_result("TC03: Password error shown")
def test_login_invalid_password(browserInstance, credentials):
    user = credentials["invalid_password"]
    login = LoginPage(browserInstance)

    login.navigate()
    login.assert_invalid_password(user["email"], user["password"])


@allure.feature("Login")
@allure.story("Blank email Login")
@pytest.mark.expected_result("TC04: Email required validation")
def test_login_empty_email(browserInstance, credentials):
    login = LoginPage(browserInstance)

    login.navigate()
    login.assert_email_required()


@allure.feature("Login")
@allure.story("Blank password Login")
@pytest.mark.expected_result("TC05: Password required validation")
def test_login_empty_password(browserInstance, credentials):
    user = credentials["valid_user"]
    login = LoginPage(browserInstance)

    login.navigate()
    login.assert_password_required(user["email"])


@allure.feature("Home page")
@allure.story("About us page navigation")
def test_about_us_navigation(browserInstance):
    login = LoginPage(browserInstance)
    login.navigate()
    login.about_us_navigation()


@allure.feature("Home page")
@allure.story("Terms of service navigation")
def test_terms_of_service_navigation(browserInstance):
    login = LoginPage(browserInstance)
    login.navigate()
    login.click_terms_of_service()


@allure.feature("Home page")
@allure.story("Privacy policy navigation")
def test_privacy_policy_navigation(browserInstance):
    login = LoginPage(browserInstance)
    login.navigate()
    login.click_privacy_policy()


@allure.feature("Home page")
@allure.story("Home page navigation")
def test_home_page_navigation(browserInstance):
    login = LoginPage(browserInstance)
    login.navigate()
    login.home_page_navigation()
