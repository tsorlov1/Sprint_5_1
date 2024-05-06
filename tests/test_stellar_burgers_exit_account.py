from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import StellarBurgersLocators


class Test_Stellar_Burgers_Exit:
    def test_stellar_burgers_exit(self, driver, login, personal_account):
        # Нажми кнопку «Выход»
        driver.find_element(*StellarBurgersLocators.BUTTON_EXIT).click()
        # Добавь явное ожидание для загрузки страницы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))
        # Проверь, что текущий url равен https://stellarburgers.nomoreparties.site/login
        assert driver.current_url == f'{URL}login'
