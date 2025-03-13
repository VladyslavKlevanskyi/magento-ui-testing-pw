import pytest

from playwright.sync_api import BrowserContext
from pages.create_account import CreateAccount
from pages.eco_friendly import CollectionsEcoFriendly
from pages.sale import Sale


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def create_account_page(page):
    return CreateAccount(page)


@pytest.fixture()
def collections_eco_friendly_page(page):
    return CollectionsEcoFriendly(page)


@pytest.fixture()
def sale_page(page):
    return Sale(page)
