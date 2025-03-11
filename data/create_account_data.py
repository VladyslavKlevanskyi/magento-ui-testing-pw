import os

from dotenv import load_dotenv
from faker import Faker

fake = Faker()

load_dotenv()

title = "Create New Customer Account"
h1_text = "Create New Customer Account"

EXISTING_USER_DATA = {
    "first_name": os.getenv("first_name"),
    "last_name": os.getenv("last_name"),
    "email": os.getenv("email"),
    "password": os.getenv("password")
}

VALID_DATA = {
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "email": fake.email(),
    "password": fake.password()
}

INVALID_DATA = {
    "first_name": "",
    "last_name": "",
    "email": "email",
    "password": "test",
    "password_conf": "Test"
}
MESSAGES = {
    "successful_registration": "Thank you for registering with Main "
                               "Website Store.",
    "required_field": "This is a required field.",
    "enter_valid_email": "Please enter a valid email address "
                         "(Ex: johndoe@domain.com).",
    "pass_strength_no_pass": "No Password",
    "pass_strength_weak": "Weak",
    "pass_strength_medium": "Medium",
    "pass_strength_strong": "Strong",
    "pass_strength_very_strong": "Very Strong",
    "minimum_pass_length": "Minimum length of this field must be equal or "
                           "greater than 8 symbols. Leading and trailing "
                           "spaces will be ignored.",
    "password_mismatch": "Please enter the same value again."
}

INVALID_EMAIL = [
    ("Empty", ("", MESSAGES["required_field"])),
    ("Without local part", ("@domain.com", MESSAGES["enter_valid_email"])),
    ("Without @", ("domain.com", MESSAGES["enter_valid_email"])),
    ("Without domain name", ("johndoe@.com", MESSAGES["enter_valid_email"])),
    ("Without dot", ("johndoe@domaincom", MESSAGES["enter_valid_email"])),
    ("Without domain zone", (
        "johndoe@domain.", MESSAGES["enter_valid_email"]
    )),
    ("Only one letter in the domain zone", (
        "johndoe@domain.c", MESSAGES["enter_valid_email"]
    )),
]

PASS_STRENGTH = [
    ("No Password", ("", MESSAGES["pass_strength_no_pass"])),
    ("Weak", ("123", MESSAGES["pass_strength_weak"])),
    ("Medium", ("123_tes_", MESSAGES["pass_strength_medium"])),
    ("Strong", ("123_test1", MESSAGES["pass_strength_strong"])),
    ("Very Strong", ("123_TesT_123", MESSAGES["pass_strength_very_strong"])),
]
