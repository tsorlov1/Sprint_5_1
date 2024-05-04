import pytest
from selenium import webdriver
from config import URL, RESOLUTION
from locators import StellarBurgersLocators


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--window-size={RESOLUTION[0]}, {RESOLUTION[1]}')
    return chrome_options

@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=browser_settings())
    driver.get(URL)
    yield  driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOGIN).send_keys("korneeva2506@gmail.com")
    driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys("123456")
    driver.find_element(*StellarBurgersLocators.BUTTON).click()
