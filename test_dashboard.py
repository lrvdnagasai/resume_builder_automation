import time

import allure
import pytest

from page.dashboard_page import DashboardPage


@allure.feature("Dashboard")
@allure.story("Dashboard page load")
@pytest.mark.smoke
def test_dashboard_page_load(authenticated_page):
    dashboard = DashboardPage(authenticated_page)

    with allure.step("Verify dashboard page loaded"):
        assert dashboard.is_dashboard_loaded()
        time.sleep(5)



@allure.feature("Dashboard")
@allure.story("Dashboard cards visibility")
@pytest.mark.smoke
def test_dashboard_cards_visible(authenticated_page):
    dashboard = DashboardPage(authenticated_page)
    time.sleep(2)
    with allure.step("Verify From Scratch card"):
        assert dashboard.from_scratch_card.is_visible()

    with allure.step("Verify Upload Resume card"):
        assert dashboard.upload_resume_card.is_visible()

    with allure.step("Verify Tailored with JD card"):
        assert dashboard.tailored_jd_card.is_visible()


@allure.feature("Dashboard")
@allure.story("Sidebar menu items")
@pytest.mark.smoke
def test_dashboard_sidebar_items(authenticated_page):
    dashboard = DashboardPage(authenticated_page)

    assert dashboard.dashboard_menu.is_visible()
    assert dashboard.all_templates_menu.is_visible()
    assert dashboard.your_resumes_menu.is_visible()
    assert dashboard.expert_review.is_visible()


@allure.feature("Dashboard")
@allure.story("Upload resume")
def test_upload_resume_click(authenticated_page):
    dashboard = DashboardPage(authenticated_page)

    with allure.step("Click Upload Resume"):
        dashboard.click_upload_resume()

    with allure.step("Verify file upload input visible"):
        assert authenticated_page.locator("input[type='file']").is_visible()


@allure.feature("Dashboard")
@allure.story("LinkedIn auto-fill option")
def test_autofill_linkedin(authenticated_page):
    dashboard = DashboardPage(authenticated_page)

    assert dashboard.linkedin_button.is_visible()


@allure.feature("Dashboard")
@allure.story("Logout")
def test_dashboard_logout(authenticated_page):
    dashboard = DashboardPage(authenticated_page)

    dashboard.logout_menu.click()
    authenticated_page.wait_for_url("**/auth**")
    assert "auth" in authenticated_page.url

