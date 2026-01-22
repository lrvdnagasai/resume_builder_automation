from playwright.sync_api import expect


class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.upload_resume_card = page.locator("text=Dashboard")

    def verify_upload_resume_visible(self):
        expect(self.upload_resume_card).to_be_visible()