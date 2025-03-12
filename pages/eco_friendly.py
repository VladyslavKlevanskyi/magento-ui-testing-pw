import random

from playwright.sync_api import expect
from data.urls import ECO_FRIENDLY_URL
from pages.base_page import BasePage
from pages.locator import common_locators as comm_locators


class CollectionsEcoFriendly(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = ECO_FRIENDLY_URL

    def check_number_of_products_is(self, number):
        all_products = self.page.locator(comm_locators.product)
        expect(all_products).to_have_count(number)

    def add_product_to_cart(self):
        product = self.page.locator(comm_locators.product).first
        product.hover()
        product.locator(comm_locators.size_element).first.click()
        product.locator(comm_locators.color_element).first.click()
        product.locator(comm_locators.add_to_cart_button).click()

    def check_number_of_products_in_cart_is(self, number):
        counter_number = self.page.locator(
            comm_locators.counter_number
        )
        expect(counter_number).to_contain_text(str(number))

    def go_to_product_page(self):
        all_products = self.page.locator(comm_locators.product).all()
        random_product = all_products[
            random.randint(0, len(all_products) - 1)
        ]
        product_name = random_product.locator(
            comm_locators.product_name
        ).inner_text()
        random_product.click()
        h1_text = self.page.locator(comm_locators.tag_h1)
        expect(h1_text).to_contain_text(product_name)
