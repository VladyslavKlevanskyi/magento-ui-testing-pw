import random

from playwright.sync_api import expect, Page
from data.urls import ECO_FRIENDLY_URL
from pages.base_page import BasePage
from pages.locator import common_locators as comm_locators


class CollectionsEcoFriendly(BasePage):
    """
    CollectionsEcoFriendly class represents the page for the 'Eco Friendly'
    collection.
    It includes methods to interact with the products in the collection,
    such as checking the number of products, adding products to the cart, and
    navigating to product pages.
    """
    def __init__(self, page: Page) -> None:
        """
        Initializes the CollectionsEcoFriendly page by setting the page URL
        for the Eco Friendly collection.

        Args:
            page (Page): The Playwright page object used to interact with the
            web page.
        """
        super().__init__(page)
        self.page_url = ECO_FRIENDLY_URL

    def check_number_of_products_is(self, number: int) -> None:
        """
        Verifies if the number of products displayed on the Eco Friendly
        collection page is equal to the expected number.

        Args:
            number (int): The expected number of products on the page.
        """
        # Locate all product elements on the page using the common locator
        # for products
        all_products = self.page.locator(comm_locators.product)
        # Verify that the number of product elements matches the expected count
        expect(all_products).to_have_count(number)

    def add_product_to_cart(self) -> None:
        """
        Adds the first product in the Eco Friendly collection to the
        shopping cart.
        This involves hovering over the product, selecting its size and color,
        and clicking the 'Add to Cart' button.
        """
        # Locate the first product on the page using the common locator
        # for products
        product = self.page.locator(comm_locators.product).first

        # Hover over the product to reveal interactive elements like size
        # and color selection
        product.hover()

        # Select the first available size option for the product
        product.locator(comm_locators.size_element).first.click()

        # Select the first available color option for the product
        product.locator(comm_locators.color_element).first.click()

        # Click the 'Add to Cart' button to add the selected product to
        # the cart
        product.locator(comm_locators.add_to_cart_button).click()

    def check_number_of_products_in_cart_is(self, number: int) -> None:
        """
        Verifies if the number of products in the shopping cart is equal to
        the expected number.

        Args:
            number (int): The expected number of products in the cart.
        """
        # Locate the element displaying the current product count in the cart
        counter_number = self.page.locator(
            comm_locators.counter_number
        )

        # Verify that the text within the counter element matches the
        # expected number of products
        expect(counter_number).to_contain_text(str(number))

    def go_to_product_page(self) -> None:
        """
        Navigates to a random product's page from the Eco Friendly collection
        and verifies that the correct product page is opened.
        """
        # Locate all product elements in the collection using the common
        # locator for products
        all_products = self.page.locator(comm_locators.product).all()

        # Select a random product from the list of products
        random_product = all_products[
            random.randint(0, len(all_products) - 1)
        ]

        # Get the product name for verification later
        product_name = random_product.locator(
            comm_locators.product_name
        ).inner_text()

        # Click on the selected random product to navigate to its product page
        random_product.click()

        # Locate the <h1> tag on the product page, which should contain the
        # product name
        h1_text = self.page.locator(comm_locators.tag_h1)

        # Verify that the <h1> tag contains the name of the product
        expect(h1_text).to_contain_text(product_name)
