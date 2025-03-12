from playwright.sync_api import Page, expect
from data.urls import BASE_URL
from pages.locator import common_locators as comm_locators


class BasePage:
    """
    BasePage class provides common functionality for interacting with web
    pages.
    It includes methods for opening a page, verifying title and headings,
    and interacting with common page elements like search fields and logo.
    """

    def __init__(self, page: Page) -> None:
        """
        Initializes the BasePage object with the given Playwright Page object.

        Args:
            page (Page): The Playwright page object for interacting with the
             page.
        """
        self.base_url = BASE_URL
        self.page_url = None
        self.page = page

    def open_page(self) -> None:
        """
        Opens the page by navigating to the full URL (base URL + page URL).
        Raises NotImplementedError if page_url is not set.

        Raises:
            NotImplementedError: If the page_url attribute is not set.
        """
        if self.page_url:
            self.page.goto(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError(
                "Page can not be opened for this page class"
            )

    def check_title_is(self, text: str) -> None:
        """
        Verifies if the page title matches the given text.

        Args:
            text (str): The expected page title.
        """
        expect(self.page).to_have_title(text)

    def check_h1_is(self, text: str) -> None:
        """
        Verifies if the <h1> element contains the given text.

        Args:
            text (str): The expected text inside the <h1> element.
        """
        h1 = self.page.locator(comm_locators.tag_h1)
        expect(h1).to_have_text(text)

    def click_logo(self) -> None:
        """
        Clicks the logo on the page.

        This assumes that the logo element locator is defined in the
        common_locators.
        """
        self.page.locator(comm_locators.logo).click()

    def check_if_the_search_field_will_find_existing_product(
            self, product_name: str
    ) -> None:
        """
        Searches for a product in the search field and checks if the results
        contain the product.

        Args:
            product_name (str): The name of the product to search for.
        """
        # Locate the search field using the locator from common_locators
        search_field = self.page.locator(comm_locators.search_field_id)

        # Fill the search field with the product name to search for it
        search_field.fill(product_name)
        search_field.press("Enter")

        # Locate the products that appear in the search results
        products = self.page.locator(comm_locators.product_name)

        # Verify that the first product in the results contains the expected
        # product name
        expect(products.first).to_contain_text(product_name)

    def check_search_field_will_not_find_nonexistent_product(
            self, product_name: str
    ) -> None:
        """
        Searches for a non-existent product and checks if the correct message
        is displayed.

        Args:
            product_name (str): The name of the non-existent product to
            search for.
        """
        # Locate the search field using the locator from common_locators
        search_field = self.page.locator(comm_locators.search_field_id)
        # Fill the search field with the product name to search for it
        search_field.fill(product_name)
        search_field.press("Enter")

        # Locate the message that appears when no products are found
        message = self.page.locator(comm_locators.search_result_message)

        # Verify that the message contains the expected text indicating
        # no results
        expect(message).to_have_text("Your search returned no results.")

    def click_create_an_account_button(self) -> None:
        """
        Clicks the 'Create an Account' button, using a locator that is
        defined in the common_locators.

        The locator for the button is expected to be defined by its role
        and name.
        """
        # Retrieve the locator information for the 'Create an Account' button
        link, text = comm_locators.registration_button_role

        # Locate the 'Create an Account' button using its role and name
        create_account_button = self.page.get_by_role(link, name=text)

        # Click the located 'Create an Account' button
        create_account_button.click()
