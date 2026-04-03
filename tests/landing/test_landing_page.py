import allure
import pytest
from page.landing.landing_page import LandingPage
from page.dashboard.dashboard_page import DashboardPage


@allure.feature("Landing Page")
@allure.story("Landing page header buttons visibility")
@pytest.mark.smoke
def test_header_elements(landing_page_auth):
    landingPage = LandingPage(landing_page_auth)

    with allure.step("Verify landing page loaded"):
        assert landingPage.is_landing_page_loaded()

    with allure.step("Verify Expert Review button"):
        assert landingPage.Expert_review_button.is_visible()

    with allure.step("Verify Examples button"):
        assert landingPage.Examples_button.is_visible()

    with allure.step("Verify Roast button"):
        assert landingPage.Roast_button.is_visible()

    with allure.step("Verify Blogs button"):
        assert landingPage.Blogs_button.is_visible()

    with allure.step("Verify Dashboard button"):
        assert landingPage.Dashboard_button.is_visible()

@allure.feature("Landing Page")
@allure.story("Dashboard navigation from header")
def test_dashboard_navigation(landing_page_auth):
    landingPage = LandingPage(landing_page_auth)

    with allure.step("Verify landing page loaded"):
        assert landingPage.is_landing_page_loaded()

    with allure.step("Click Dashboard button in header"):
        landingPage.click_dashboard()

    with allure.step("Verify navigated to dashboard page"):
        dashboard = DashboardPage(landing_page_auth)
        assert dashboard.is_dashboard_loaded(), "Dashboard page did not load after clicking Dashboard button"


