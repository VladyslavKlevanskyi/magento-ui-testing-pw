from data.urls import CREATE_ACCOUNT_URL
from pages.base_page import BasePage
from pages.locator import create_account_locators as locators
from playwright.sync_api import expect, Page


class CreateAccount(BasePage):
    """
    CreateAccount class represents the page and actions related to creating
    a user account.
    It includes methods to interact with the page elements required for
    account creation, such as filling in user details and verifying the
    success or failure of the registration.
    """
    def __init__(self, page: Page) -> None:
        """
        Initializes the CreateAccount page by setting the page URL for
        account creation.

        Args:
            page (Page): The Playwright page object used to interact with
            the web page.
        """
        super().__init__(page)
        self.page_url = CREATE_ACCOUNT_URL

    def enter_first_name(self, first_name: str) -> None:
        """
        Fills in the 'First Name' field with the given first name.

        Args:
            first_name (str): The first name to enter into the form.
        """
        # Locate the 'First Name' field using its ID from locators
        first_name_field = self.page.locator(locators.first_name_id)
        # Fill the 'First Name' field with the provided first name
        first_name_field.fill(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """
        Fills in the 'Last Name' field with the given last name.

        Args:
            last_name (str): The last name to enter into the form.
        """
        # Locate the 'Last Name' field using its ID from locators
        last_name_field = self.page.locator(locators.last_name_id)
        # Fill the 'Last Name' field with the provided last name
        last_name_field.fill(last_name)

    def enter_email(self, email: str) -> None:
        """
        Fills in the 'Email' field with the given email address.

        Args:
            email (str): The email address to enter into the form.
        """
        # Locate the 'Email' field using its ID from locators
        email_field = self.page.locator(locators.email_id)
        # Fill the 'Email' field with the provided email address
        email_field.fill(email)

    def enter_password(self, password: str) -> None:
        """
        Fills in the 'Password' field with the given password.

        Args:
            password (str): The password to enter into the form.
        """
        # Locate the 'Password' field using its ID from locators
        password_field = self.page.locator(locators.password_id)
        # Enter the password into the field with a sequential delay
        password_field.press_sequentially(password,  delay=100)

    def enter_password_confirmation(self, password: str) -> None:
        """
        Fills in the 'Password Confirmation' field with the given password.

        Args:
            password (str): The password to confirm in the confirmation field.
        """
        # Locate the 'Password Confirmation' field using its ID from locators
        password_confirmation_field = self.page.locator(
            locators.password_confirmation_id
        )
        # Fill the 'Password Confirmation' field with the provided password
        password_confirmation_field.fill(password)

    def click_create_an_account_button(self) -> None:
        """
        Clicks the 'Create an Account' button to submit the registration form.
        """
        # Locate the 'Create an Account' button using its XPath from locators
        submit_button = self.page.locator(locators.submit_button_xpath)
        # Click the submit button to attempt account creation
        submit_button.click()

    def check_successful_account_creation_alert_is(self, text: str) -> None:
        """
        Verifies if the success alert message is displayed after account
        creation.

        Args:
            text (str): The expected text in the success alert message.
        """
        # Locate the success alert message using its XPath from locators
        alert = self.page.locator(
            locators.successful_registration_alert_xpath
        ).first
        # Verify that the alert contains the expected success message
        expect(alert).to_have_text(text)

    def check_field_alert_is(self, field_name: str, message: str) -> None:
        """
        Checks if the alert message for a specific field is displayed with
        the given message.

        Args:
            field_name (str): The name of the field to check
            (e.g., 'First Name', 'Email').
            message (str): The expected alert message for the field.
        """
        # Initialize the alert variable
        alert = None

        # Check the appropriate field's alert based on the field name
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

        # Verify that the field's alert contains the expected message
        expect(alert).to_have_text(message)
