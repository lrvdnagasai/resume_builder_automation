import time
from pathlib import Path

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
        dashboard.page.wait_for_selector("text=Welcome")

        #time.sleep(5)



@allure.feature("Dashboard")
@allure.story("Dashboard cards visibility")
#@pytest.mark.smoke
def test_dashboard_cards_visible(authenticated_page):
    dashboard = DashboardPage(authenticated_page)
    dashboard.from_scratch_card.wait_for(state="visible")
    with allure.step("Verify From Scratch card"):
        assert dashboard.from_scratch_card.is_visible()

    with allure.step("Verify Upload Resume card"):
        assert dashboard.upload_resume_card.is_visible()

    with allure.step("Verify Tailored with JD card"):
        assert dashboard.tailored_jd_card.is_visible()


@allure.feature("Dashboard")
@allure.story("Sidebar menu items")
#@pytest.mark.smoke
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

    file_path = Path(__file__).parent / "test_data" / "Nagasai__Resume-1.pdf"

    with allure.step("Click Upload Resume and select file"):
        dashboard.upload_resume_file(str(file_path))
        time.sleep(5)

    with allure.step("Verify Pika Extract processing screen appears"):
        assert dashboard.is_file_uploaded_successfully(), "Pika Extract screen did not appear after upload"


@allure.feature("Dashboard")
@allure.story("LinkedIn auto-fill option")
def test_autofill_linkedin(authenticated_page):
    dashboard = DashboardPage(authenticated_page)

    assert dashboard.linkedin_button.is_visible()

@allure.feature("Dashboard")
@allure.story("autofill Linkedin popup verification")
def test_linkedin_popup_loads(authenticated_page):
    dashboard = DashboardPage(authenticated_page)
    dashboard.click_autofill_via_linkedin()
    assert dashboard.linkedin_popup_text.is_visible()


@allure.feature("Dashboard")
@allure.story("Linkedin popup close button")
def test_linkedin_popup_close_button(authenticated_page):
    dashboard = DashboardPage(authenticated_page)
    dashboard.click_autofill_via_linkedin()
    dashboard.close_button_linkedin_popup()

@allure.feature("Dashboard")
@allure.story("Logout")
def test_dashboard_logout(authenticated_page):
    dashboard = DashboardPage(authenticated_page)

    dashboard.logout_menu.click()
    authenticated_page.wait_for_url("**/auth**")
    assert "auth" in authenticated_page.url

@allure.feature("Dashboard")
@allure.story("Linkedin Autofill verification")
def test_linkedin_autofill(authenticated_page):
    dashboard = DashboardPage(authenticated_page)
    dashboard.click_autofill_via_linkedin()
    dashboard.fill_linkedin_url()
    dashboard.click_convert_resume_button()
    assert dashboard.verify_linkedin_extract_screen()
    