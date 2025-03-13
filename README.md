# Playwright Autotests Portfolio

## About the Project
This project is a portfolio showcasing automated tests written using [Playwright](https://playwright.dev/) and `pytest`. 
Playwright is a modern tool for end-to-end testing of web applications, supporting multiple browsers.
The tests in this project are organized using the Page Object Model (POM) design pattern, which helps to separate the test logic from the web page structure. This approach improves the maintainability and readability of the tests, as each page of the web application is represented by a separate class with methods that interact with its elements.

## Technologies Used
- **Playwright** - for browser automation
- **Python** - programming language for writing tests
- **pytest** - testing framework
- **Allure Report** - test report generation (optional)

## Installation
### 1. Clone the repository
```bash
git clone https://github.com/VladyslavKlevanskyi/magento-ui-testing-pw.git
cd magento-ui-testing-pw
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running Tests
### Run all tests
```bash
pytest
```

### Run a specific test
```bash
pytest test/test_create_account.py
pytest test/test_eco_friendly.py
pytest test/test_sale.py
```

### Run tests with Allure report (if used)
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Project Structure
```
📂 your-repository  
├── 📂 test                            # Directory with test cases  
│   ├── test_create_account.py         # Test cases for the create account page functionality  
│   ├── test_eco_friendly.py           # Test cases for the eco-friendly page functionality  
│   └── test_sale.py                   # Test cases for the sale page functionality  
├── 📂 data                            # Files with data for tests  
├── 📂 pages                           # Page Object Model classes and locators for web pages  
│   ├── 📂 locator                     # Folder containing locators for page elements  
│   │   ├── common_locators.py          # Common locators used across multiple pages  
│   │   └── create_account_locators.py  # Locators specific to the create account page  
│   ├── base_page.py                    # Base class with common methods for all pages  
│   ├── create_account.py               # Page class for the create account page  
│   ├── eco_friendly.py                 # Page class for the eco-friendly page  
│   └── sale.py                         # Page class for the sale page  
├── requirements.txt                    # Project dependencies  
├── pytest.ini                          # Playwright configuration  
├── conftest.py                         # pytest setup file  
└── README.md                           # Project description
```
