from playwright.sync_api import Page
import allure
class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

        # Header
        self.welcome_text = page.get_by_text("Welcome", exact=False)

        # Dashboard Cards
        self.from_scratch_card = page.get_by_text("From Scratch")
        self.upload_resume_card = page.get_by_text("Upload Resume")
        self.tailored_jd_card = page.get_by_text("Tailored with JD")
        self.uploadresume_button = page.locator('div.border-purple-500:has-text("Upload Resume")')
        self.dashboard_menu = page.get_by_role("link", name="Dashboard")
        self.all_templates_menu = page.get_by_role("link", name="All Templates")
        self.your_resumes_menu = page.get_by_role("link", name="Your Resumes")
        self.logout_menu = page.get_by_text("Logout", exact=True)
        self.expert_review = page.get_by_role("link", name="Expert Review")
        self.pika_extract_text = page.locator("h3.text-white:has-text('Pika Extract')")
        self.linkedin_button = page.get_by_role("button", name="Auto-fill via Linkedin")
        self.linkedin_popup_text = page.get_by_role("heading", name="From LinkedIn to Resume", exact=True)
        self.enter_linkedin_url = page.get_by_role("textbox", name="linkedin.com/in/your.name")
        self.convert_resume_button = page.get_by_role("button", name="Convert to Resume")
        self.linkedin_popup_closebutton = page.get_by_label("close")
        self.linkedin_extract_text = page.get_by_text("Extracting profile data...")
        self.download_pdf_button = page.get_by_role("button", name="Download PDF")
    @allure.step("Welcome page")
    def is_dashboard_loaded(self):
        return self.welcome_text.is_visible()
    @allure.step("Click upload resume")
    def click_upload_resume(self):
        self.uploadresume_button.click()

    @allure.step("Verify file upload dialog triggered")
    def is_file_input_present(self):
        return self.page.locator("input[type='file']").count() > 0

    @allure.step("Upload resume file")
    def upload_resume_file(self, file_path: str):
        file_input = self.page.locator("input[type='file']")
        file_input.set_input_files(file_path)

    @allure.step("Verify file upload success - Pika Extract screen")
    def is_file_uploaded_successfully(self):
        self.pika_extract_text.wait_for(state="visible", timeout=15000)
        return self.pika_extract_text.is_visible()

    @allure.step("click autofill via linkedin")
    def click_autofill_via_linkedin(self):
        self.linkedin_button.click()

    @allure.step("click linkedin popup close button")
    def close_button_linkedin_popup(self):
        self.linkedin_popup_closebutton.click()

    @allure.step("Fill linkedin URL")
    def fill_linkedin_url(self):
        self.enter_linkedin_url.fill("https://www.linkedin.com/in/nagasai-lakkoju-41628a115/")

    @allure.step("click convert resume button")
    def click_convert_resume_button(self):
        self.convert_resume_button.click()


    @allure.step("Verify Linkedin extract screen appears")
    def verify_linkedin_extract_screen(self):
        self.linkedin_extract_text.wait_for(state="visible", timeout=15000)
        return self.linkedin_extract_text.is_visible()