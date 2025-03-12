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

    def check_title_is(self, text):
        expect(self.page).to_have_title(text)

    def check_h1_is(self, text):
        h1 = self.page.locator(comm_locators.tag_h1)
        expect(h1).to_have_text(text)

    def click_logo(self):
        self.page.locator(comm_locators.logo).click()

    def check_if_the_search_field_will_find_existing_product(
            self, product_name: str
    ):
        search_field = self.page.locator(comm_locators.search_field_id)
        search_field.fill(product_name)
        search_field.press("Enter")
        products = self.page.locator(comm_locators.product_name)
        expect(products.first).to_contain_text(product_name)

    def check_search_field_will_not_find_nonexistent_product(
            self, product_name: str
    ):
        search_field = self.page.locator(comm_locators.search_field_id)
        search_field.fill(product_name)
        search_field.press("Enter")
        message = self.page.locator(comm_locators.search_result_message)
        expect(message).to_have_text("Your search returned no results.")

    def check_create_an_account_button_functionality(self):
        link, text = comm_locators.registration_button_role
        create_account_button = self.page.get_by_role(link, name=text)
        create_account_button.click()
        expect(self.page).to_have_title("Create New Customer Account")
