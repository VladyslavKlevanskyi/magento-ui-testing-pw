import pytest

from data import product_data
from data.create_account_data import (
    title,
    h1_text,
    VALID_DATA,
    INVALID_DATA,
    MESSAGES,
    INVALID_EMAIL,
    PASS_STRENGTH
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
    create_account_page.click_logo()
    create_account_page.check_title_is(text="Home Page")


@pytest.mark.high
def test_search_field_functionality(create_account_page):
    create_account_page.open_page()
    create_account_page.check_if_the_search_field_will_find_existing_product(
        product_name=product_data.valid_product_name
    )
    create_account_page.check_search_field_will_not_find_nonexistent_product(
        product_name=product_data.invalid_product_name
    )


@pytest.mark.smoke
def test_create_account_with_valid_data(create_account_page):
    create_account_page.open_page()
    create_account_page.enter_first_name(first_name=VALID_DATA["first_name"])
    create_account_page.enter_last_name(last_name=VALID_DATA["last_name"])
    create_account_page.enter_email(email=VALID_DATA["email"])
    create_account_page.enter_password(password=VALID_DATA["password"])
    create_account_page.enter_password_confirmation(
        password=VALID_DATA["password"]
    )
    create_account_page.click_create_an_account_button()
    create_account_page.check_successful_account_creation_alert_is(
        MESSAGES["successful_registration"]
    )


@pytest.mark.smoke
def test_create_account_with_invalid_data(create_account_page):
    create_account_page.open_page()
    create_account_page.enter_first_name(first_name=INVALID_DATA["first_name"])
    create_account_page.enter_last_name(last_name=INVALID_DATA["last_name"])
    create_account_page.enter_email(email=INVALID_DATA["email"])
    create_account_page.enter_password(password=INVALID_DATA["password"])
    create_account_page.enter_password_confirmation(
        password=INVALID_DATA["password_conf"]
    )
    create_account_page.click_create_an_account_button()
    create_account_page.check_field_alert_is(
        field_name="First Name",
        message=MESSAGES["required_field"]
    )
    create_account_page.check_field_alert_is(
        field_name="Last Name",
        message=MESSAGES["required_field"]
    )
    create_account_page.check_field_alert_is(
        field_name="Email",
        message=MESSAGES["enter_valid_email"]
    )
    create_account_page.check_field_alert_is(
        field_name="Pass Strength",
        message=MESSAGES["pass_strength_weak"]
    )
    create_account_page.check_field_alert_is(
        field_name="Pass",
        message=MESSAGES["minimum_pass_length"]
    )
    create_account_page.check_field_alert_is(
        field_name="Pass Confirmation",
        message=MESSAGES["password_mismatch"]
    )


@pytest.mark.critical
def test_first_and_last_name_fields_are_required(create_account_page):
    create_account_page.open_page()
    create_account_page.click_create_an_account_button()
    create_account_page.check_field_alert_is(
        field_name="First Name",
        message=MESSAGES["required_field"]
    )
    create_account_page.check_field_alert_is(
        field_name="Last Name",
        message=MESSAGES["required_field"]
    )


@pytest.mark.critical
@pytest.mark.parametrize(
    argnames="email, message",
    argvalues=[data[1] for data in INVALID_EMAIL],
    ids=[title[0] for title in INVALID_EMAIL]
)
def test_email_field_validation(create_account_page, email, message):
    create_account_page.open_page()
    create_account_page.enter_email(email=email)
    create_account_page.click_create_an_account_button()
    create_account_page.check_field_alert_is(
        field_name="Email",
        message=message
    )


@pytest.mark.medium
@pytest.mark.parametrize(
    argnames="password, message",
    argvalues=[data[1] for data in PASS_STRENGTH],
    ids=[title[0] for title in PASS_STRENGTH]
)
def test_password_strength_validation(create_account_page, password, message):
    create_account_page.open_page()
    create_account_page.enter_password(password=password)
    create_account_page.check_field_alert_is(
        field_name="Pass Strength",
        message=message
    )
