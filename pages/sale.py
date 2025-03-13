from playwright.sync_api import Page
from data.urls import SALE_URL
from pages.base_page import BasePage


class Sale(BasePage):
    """
    Sale class represents the page for the 'Sale' section of the website.
    It inherits from the BasePage class and contains the URL specific to the
    Sale page.
    """
    def __init__(self, page: Page):
        """
        Initializes the Sale page by setting the page URL for the Sale section.

        Args:
            page (Page): The Playwright page object used to interact with the
            web page.
        """
        super().__init__(page)
        self.page_url = SALE_URL
