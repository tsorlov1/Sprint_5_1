import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import StellarBurgersLocators
from helpers import get_sign_up_data


class Test_Stellar_Burgers_Registration:

    def test_stellar_burgers_registration(self, driver):
        driver.get(f'{URL}register')
        # Выполни регистрацию
        name_data, email_data, password_data = get_sign_up_data()
        driver.find_element(*StellarBurgersLocators.NAME_FIELD_REGISTRATION).send_keys(name_data)
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_REGISTRATION).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*StellarBurgersLocators.BUTTON).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))
        # Проверь, что текущий url равен hhttps://stellarburgers.nomoreparties.site/login
        assert driver.current_url == f'{URL}login'


    def test_stellar_burgers_registration_password_error(self, driver):
        driver.get(f'{URL}register')
        # Выполни регистрацию c ошибкой в пароле
        name_data, email_data, password_data = get_sign_up_data()
        driver.find_element(*StellarBurgersLocators.NAME_FIELD_REGISTRATION).send_keys(name_data)
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_REGISTRATION).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys((f"{random.randint(1, 99999)}"))
        driver.find_element(*StellarBurgersLocators.BUTTON).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.PASSWORD_ERROR_REGISTRATION))
        # Проверь, что текущий url равен https://stellarburgers.nomoreparties.site/register
        assert driver.current_url == f'{URL}register'
