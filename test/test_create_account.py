import pytest

from data.create_account_data import (
    title,
    h1_text,
)


@pytest.mark.medium
def test_page_h1_header(create_account_page):
    create_account_page.open_page()
    create_account_page.check_h1_is(text=h1_text)


@pytest.mark.low
def test_page_title(create_account_page):
    create_account_page.open_page()
    create_account_page.check_title_is(text=title)


@pytest.mark.high
def test_click_on_logo_redirects_to_home_page(create_account_page):
    create_account_page.open_page()
    create_account_page.check_logo_clickability()
