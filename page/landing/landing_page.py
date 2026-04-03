import allure
from playwright.sync_api import Page


class LandingPage:
    def __init__(self, page: Page):
        self.page = page

        # Scope all header buttons to the header element
        self.header = page.locator("header")

        self.text_on_homepage = page.get_by_role("heading", name="4 Ways to Build Your", exact=False)
        self.Expert_review_button = self.header.get_by_role("button", name="Expert Review", exact=True)
        self.Roast_button = self.header.get_by_role("button", name="Roast", exact=True)
        self.Blogs_button = self.header.get_by_role("button", name="Blogs", exact=True)
        self.Examples_button = self.header.get_by_role("button", name="Examples", exact=True)
        self.Dashboard_button = self.header.get_by_role("button", name="Dashboard", exact=True)
        self.Home_button = self.header.get_by_role("button", name="Home", exact=True)

    @allure.step("Verify landing page loaded")
    def is_landing_page_loaded(self):
        self.text_on_homepage.wait_for(state="visible", timeout=10000)
        return self.text_on_homepage.is_visible()

    @allure.step("Click Dashboard button in header")
    def click_dashboard(self):
        self.Dashboard_button.click()
