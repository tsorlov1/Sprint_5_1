from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import StellarBurgersLocators


class Test_Stellar_Burgers_Go_To_Constructor:
    def test_stellar_burgers_go_to_constructor_button(self, driver, login, personal_account):
        # Нажми кнопку «Конструктор»
        driver.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCTOR).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_TITLE))
        # Проверь, что текущий url равен https://stellarburgers.nomoreparties.site
        assert driver.current_url == URL


    def test_stellar_burgers_go_to_constructor_logo(self, driver, login, personal_account):
        # Нажми на Логотип
        driver.find_element(*StellarBurgersLocators.LOGO).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_TITLE))
        # Проверь, что текущий url равен https://stellarburgers.nomoreparties.site
        assert driver.current_url == URL
