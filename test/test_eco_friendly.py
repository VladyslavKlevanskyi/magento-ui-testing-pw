import allure
import pytest

from data import eco_friendly_data
from data import product_data


@allure.feature("Positive")
@allure.title("Ensure that clicking on the logo redirects to the home page.")
@pytest.mark.high
def test_click_on_logo_redirects_to_home_page(collections_eco_friendly_page):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.click_logo()


@allure.feature("Positive&Negative")
@allure.title("Ensure the search field works on this page.")
@pytest.mark.high
def test_search_field_functionality(collections_eco_friendly_page):
    collections_eco_friendly_page.open_page()
    (collections_eco_friendly_page.
        check_if_the_search_field_will_find_existing_product(
            product_name=product_data.valid_product_name
        ))
    (collections_eco_friendly_page.
        check_search_field_will_not_find_nonexistent_product(
            product_name=product_data.invalid_product_name
        ))


@allure.feature("Positive")
@allure.title(
    "Ensure the create an account button redirects to the registration page."
)
@pytest.mark.high
def test_create_an_account_button_redirects_to_registration_page(
        collections_eco_friendly_page
):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.click_create_an_account_button()
    collections_eco_friendly_page.check_title_is(
        text="Create New Customer Account"
    )


@allure.feature("Positive")
@allure.title("Ensure the product can be added to the cart")
@pytest.mark.smoke
def test_that_product_can_be_added_to_cart(collections_eco_friendly_page):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.add_product_to_cart()
    collections_eco_friendly_page.check_number_of_products_in_cart_is(number=1)


@allure.feature("Positive")
@allure.title("Ensure you can go to the product page by clicking on it")
@pytest.mark.smoke
def test_the_possibility_to_go_to_the_product_page(
        collections_eco_friendly_page
):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.go_to_product_page()


@allure.feature("Positive")
@allure.title("Ensure that the page has the correct h1 header")
@pytest.mark.medium
def test_page_h1_header(collections_eco_friendly_page):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.check_h1_is(text=eco_friendly_data.h1)


@allure.feature("Positive")
@allure.title("Ensure that the page has the correct title")
@pytest.mark.low
def test_page_title(collections_eco_friendly_page):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.check_title_is(text=eco_friendly_data.title)


@allure.feature("Positive")
@allure.title(
    "Ensure the page does not display more than the selected number of products"
)
@pytest.mark.high
def test_page_does_not_display_more_than_selected_number_of_products(
        collections_eco_friendly_page
):
    collections_eco_friendly_page.open_page()
    collections_eco_friendly_page.check_number_of_products_is(number=12)
