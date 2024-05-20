from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import StellarBurgersLocators


class Test_Stellar_Burgers_Personal_Account:
    def test_stellar_burgers_go_to_personal_account(self, driver, login):
        # Нажми кнопку «Личный кабинет»
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        # Добавь явное ожидание для загрузки страницы «Личный кабинет»
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.BUTTON_PROFILE))
        # Проверь, что текущий url равен https://stellarburgers.nomoreparties.site/account/profile
        assert driver.current_url == f'{URL}account/profile'
