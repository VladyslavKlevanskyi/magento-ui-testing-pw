import allure
import pytest

from data import sale_data
from data import product_data


@allure.feature("Positive")
@allure.title("Ensure that the page has the correct h1 header")
@pytest.mark.medium
def test_page_h1_header(sale_page):
    sale_page.open_page()
    sale_page.check_h1_is(text=sale_data.h1)


@allure.feature("Positive")
@allure.title("Ensure that the page has the correct title")
@pytest.mark.low
def test_page_title(sale_page):
    sale_page.open_page()
    sale_page.check_title_is(text=sale_data.title)


@allure.feature("Positive")
@allure.title("Ensure that clicking on the logo redirects to the home page.")
@pytest.mark.high
def test_click_on_logo_redirects_to_home_page(sale_page):
    sale_page.open_page()
    sale_page.click_logo()
    sale_page.check_title_is(text="Home Page")


@allure.feature("Positive&Negative")
@allure.title("Ensure the search field works on this page.")
@pytest.mark.high
def test_search_field_functionality(sale_page):
    sale_page.open_page()
    sale_page.check_if_the_search_field_will_find_existing_product(
        product_name=product_data.valid_product_name
    )
    sale_page.check_search_field_will_not_find_nonexistent_product(
        product_name=product_data.invalid_product_name
    )


@allure.feature("Positive")
@allure.title(
    "Ensure the create an account button redirects to the registration page."
)
@pytest.mark.high
def test_create_an_account_button_redirects_to_registration_page(sale_page):
    sale_page.open_page()
    sale_page.click_create_an_account_button()
    sale_page.check_title_is(text="Create New Customer Account")
