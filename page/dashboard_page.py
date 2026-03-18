from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

        # Header
        self.welcome_text = page.get_by_text("Welcome", exact=False)

        # Dashboard Cards
        self.from_scratch_card = page.get_by_text("From Scratch")
        self.upload_resume_card = page.get_by_text("Upload Resume")
        self.tailored_jd_card = page.get_by_text("Tailored with JD")
        self.uploadresume_button = page.get_by_role("button", name="Upload Resume")
        # Sidebar
        self.dashboard_menu = page.get_by_role("link", name="Dashboard")
        self.all_templates_menu = page.get_by_role("link", name="All Templates")
        self.your_resumes_menu = page.get_by_role("link", name="Your Resumes")
        self.logout_menu = page.get_by_role("link", name="Logout")
        self.expert_review = page.get_by_role("link", name="Expert Review")
        # Auto-fill
        self.linkedin_button = page.get_by_role(
            "button", name="Auto-fill via Linkedin"
        )

    def is_dashboard_loaded(self):
        return self.welcome_text.is_visible()

    def click_upload_resume(self):
        self.uploadresume_button.click()
