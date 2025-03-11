from playwright.sync_api import Page, expect
from data.urls import BASE_URL
from pages.locator import common_locators as comm_locators


class BasePage:

    def __init__(self, page: Page):
        self.base_url = BASE_URL
        self.page_url = None
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError(
                "Page can not be opened for this page class"
            )

    # def find(self, locator: str, element: Page = None) -> Locator:
    #     if element is None:
    #         return self.page.locator(locator)
    #     return element.locator(locator)

    # def find_all(self, locator: tuple, element: Page = None):
    #     if element is None:
    #         return self.page.locator(locator)
    #     return element.locator(locator)

    def check_title_is(self, text):
        assert self.page.title() == text

    def check_h1_is(self, text):
        h1 = self.page.locator(comm_locators.tag_h1)
        expect(h1).to_have_text(text)

    def check_logo_clickability(self):
        self.page.locator(comm_locators.logo).click()
        assert self.page.title() == "Home Page"
