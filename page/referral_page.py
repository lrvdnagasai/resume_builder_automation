
import allure
from playwright.sync_api import expect


class ReferralPage:

    def __init__(self, page):
        self.page = page

        self.referral_page_text = page.get_by_text("REFERRAL", exact=False)
        self.copy_link = page.get_by_role("button", name="Copy Link")
        

