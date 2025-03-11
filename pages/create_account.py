from data.urls import CREATE_ACCOUNT_URL
from pages.base_page import BasePage


class CreateAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = CREATE_ACCOUNT_URL
