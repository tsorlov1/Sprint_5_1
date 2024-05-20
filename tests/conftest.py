import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL, EMAIL, PASSWORD
from locators import StellarBurgersLocators


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    return chrome_options

@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=browser_settings())
    driver.get(URL)
    yield  driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get(f'{URL}login')
    driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOGIN).send_keys(EMAIL)
    driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*StellarBurgersLocators.BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.BUTTON_ORDER))


@pytest.fixture
def personal_account(driver):
    driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.BUTTON_PROFILE))


@pytest.fixture
def constructor(driver):
    driver.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCTOR).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_TITLE))
