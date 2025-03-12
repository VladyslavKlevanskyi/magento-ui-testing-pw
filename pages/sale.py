from data.urls import SALE_URL
from pages.base_page import BasePage


class Sale(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = SALE_URL
