import time

import re

from playwright.sync_api import expect

from .dashboard_page import DashboardPage


class LoginPage:
    URL = "https://pikaresume.com"

    def __init__(self, page):
        self.page = page


        self.sign_in_button = page.get_by_role("button", name="Sign In")
        self.see_other_option_button = page.get_by_role("button", name="See other Option")
        self.email_input = page.get_by_role("textbox", name="Enter email address")
        self.continue_button = page.get_by_role("button", name="Continue", exact=True)
        self.password_input = page.get_by_role("textbox", name="Enter your password")
        self.login_button = page.get_by_role("button", name="Login")
        self.about_us_button = page.get_by_role("button", name="About Us")
        self.terms_of_conditions = page.get_by_role("link", name="Terms of Service")
        self.privacy_policy = page.get_by_role("link", name="Privacy Policy")
        self.pikaResume_button = page.get_by_role("button", name='Pika Resume')


        # Validation messages
        self.invalid_email_error = page.get_by_text("Please enter a valid email")
        self.email_required_error = page.get_by_text("Email is required")
        self.invalid_password_error = page.get_by_text("Invalid password. Please try")
        self.password_required_error = page.get_by_text("Password is required*")
        self.about_us_page_text = page.get_by_role("heading", name="Meet Resume Builder")
        self.home_page_text = page.get_by_role("heading", name="Build a Professional Resume")


    def navigate(self):
        self.page.goto(self.URL)

    def open_login_form(self):
        self.sign_in_button.click()
        self.see_other_option_button.click()
        expect(self.email_input).to_be_visible()

    def submit_email(self, email: str):
        self.open_login_form()
        self.email_input.fill(email)
        self.continue_button.click()

    def submit_password(self, password: str):
        expect(self.password_input).to_be_visible()
        self.password_input.fill(password)
        self.login_button.click()

    def login_valid(self, email: str, password: str) -> DashboardPage:
        self.submit_email(email)
        expect(self.invalid_email_error).not_to_be_visible()
        expect(self.email_required_error).not_to_be_visible()
        self.submit_password(password)
        expect(self.invalid_password_error).not_to_be_visible()
        expect(self.password_required_error).not_to_be_visible()
        dashboard = DashboardPage(self.page)
        dashboard.verify_upload_resume_visible()
        return dashboard

    def assert_invalid_email_format(self, email: str):
        self.submit_email(email)
        expect(self.invalid_email_error).to_be_visible()

    def assert_email_required(self):
        self.submit_email("")
        expect(self.email_required_error).to_be_visible()

    def assert_invalid_password(self, email: str, password: str):
        self.submit_email(email)
        expect(self.invalid_email_error).not_to_be_visible()
        expect(self.email_required_error).not_to_be_visible()

        self.submit_password(password)
        expect(self.invalid_password_error).to_be_visible()

    def assert_password_required(self, email: str):
        self.submit_email(email)
        expect(self.invalid_email_error).not_to_be_visible()
        expect(self.email_required_error).not_to_be_visible()

        self.submit_password("")
        expect(self.password_required_error).to_be_visible()

    def about_us_navigation(self):
        self.sign_in_button.click()
        self.about_us_button.click()
        expect(self.about_us_page_text).to_be_visible()

    def home_page_navigation(self):
        self.sign_in_button.click()
        self.pikaResume_button.click()
        expect(self.home_page_text).to_be_visible()

    def click_terms_of_service(self):
        self.sign_in_button.click()

        before_url = self.page.url
        context = self.page.context

        # Try: link may open in a new tab OR same tab.
        try:
            with context.expect_page(timeout=2000) as new_page_info:
                self.terms_of_conditions.click()
            new_page = new_page_info.value
            new_page.wait_for_load_state("domcontentloaded")

            # Assert new page opened and looks like terms page (URL pattern)
            expect(new_page).to_have_url(re.compile(r".*(terms|terms-of-service).*", re.I))
            return new_page
        except Exception:
            # No new tab opened within 2s -> assume same tab navigation (or no navigation due to bug)
            self.terms_of_conditions.click()

            # Assert same-tab navigation happened (this will FAIL if no navigation occurs)
            expect(self.page).not_to_have_url(before_url, timeout=5000)
            expect(self.page).to_have_url(re.compile(r".*(terms|terms-of-service).*", re.I))
            return self.page

    def click_privacy_policy(self):
        self.sign_in_button.click()
        self.privacy_policy.click()

        before_url = self.page.url
        context = self.page.context

        # Try: link may open in a new tab OR same tab.
        try:
            with context.expect_page(timeout=2000) as new_page_info:
                self.privacy_policy.click()
            new_page = new_page_info.value
            new_page.wait_for_load_state("domcontentloaded")

            # Assert new page opened and looks like privacy page (URL pattern)
            expect(new_page).to_have_url(re.compile(r".*(privacy|privacy-policy).*", re.I))
            return new_page
        except Exception:
            # No new tab opened within 2s -> assume same tab navigation (or no navigation due to bug)
            self.privacy_policy.click()

            # Assert same-tab navigation happened (this will FAIL if no navigation occurs)
            expect(self.page).not_to_have_url(before_url, timeout=5000)
            expect(self.page).to_have_url(re.compile(r".*(privacy|privacy-policy).*", re.I))
            return self.page



        #git test