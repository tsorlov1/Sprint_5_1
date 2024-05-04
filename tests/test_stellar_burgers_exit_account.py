from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import StellarBurgersLocators


class Test_Stellar_Burgers_Exit:
    def test_stellar_burgers_exit(self, driver):
        # Нажми кнопку «Личный кабинет»
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        # Добавь явное ожидание для загрузки страницы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))
        # Выполни авторизацию
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOGIN).send_keys("korneeva2506@gmail.com")
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(*StellarBurgersLocators.BUTTON).click()
        # Нажми кнопку «Личный кабинет»
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.BUTTON_PROFILE))
        # Нажми кнопку «Выход»
        driver.find_element(*StellarBurgersLocators.BUTTON_EXIT).click()
        # Добавь явное ожидание для загрузки страницы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))
        # Проверь, что текущий url равен https://stellarburgers.nomoreparties.site/login
        assert driver.current_url == f'{URL}login'
