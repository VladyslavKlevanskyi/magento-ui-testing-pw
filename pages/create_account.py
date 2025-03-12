from data.urls import CREATE_ACCOUNT_URL
from pages.base_page import BasePage
from pages.locator import create_account_locators as locators
from playwright.sync_api import expect


class CreateAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = CREATE_ACCOUNT_URL

    def enter_first_name(self, first_name: str):
        first_name_field = self.page.locator(locators.first_name_id)
        first_name_field.fill(first_name)

    def enter_last_name(self, last_name: str):
        last_name_field = self.page.locator(locators.last_name_id)
        last_name_field.fill(last_name)

    def enter_email(self, email: str):
        email_field = self.page.locator(locators.email_id)
        email_field.fill(email)

    def enter_password(self, password: str):
        password_field = self.page.locator(locators.password_id)
        password_field.press_sequentially(password,  delay=100)

    def enter_password_confirmation(self, password: str):
        password_confirmation_field = self.page.locator(
            locators.password_confirmation_id
        )
        password_confirmation_field.fill(password)

    def click_create_an_account_button(self):
        submit_button = self.page.locator(locators.submit_button_xpath)
        submit_button.click()

    def check_successful_account_creation_alert_is(self, text):
        alert = self.page.locator(
            locators.successful_registration_alert_xpath
        ).first
        expect(alert).to_have_text(text)

    def check_field_alert_is(self, field_name: str, message: str):
        alert = None
        if field_name == "First Name":
            alert = self.page.locator(locators.first_name_alert_id)
        elif field_name == "Last Name":
            alert = self.page.locator(locators.last_name_alert_id)
        elif field_name == "Email":
            alert = self.page.locator(locators.email_alert_id)
        elif field_name == "Pass":
            alert = self.page.locator(locators.password_alert_id)
        elif field_name == "Pass Strength":
            alert = self.page.locator(locators.password_strength_meter_id)
        elif field_name == "Pass Confirmation":
            alert = self.page.locator(locators.password_conf_alert_id)
        expect(alert).to_have_text(message)
