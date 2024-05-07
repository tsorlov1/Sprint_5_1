from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import StellarBurgersLocators


class Test_Stellar_Burgers_Constructor:
    def test_stellar_burgers_constructor_go_to_bread(self, driver, login, personal_account, constructor):
        # Нажми кнопку «Начинки»
        driver.find_element(*StellarBurgersLocators.FILLINGS).click()
        # Нажми кнопку «Булки»
        driver.find_element(*StellarBurgersLocators.BREAD).click()
        # Найди заголовок, получи его текст и проверь, что он равен 'Булки'
        assert driver.find_element(*StellarBurgersLocators.BREAD).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


    def test_stellar_burgers_constructor_go_to_sause(self, driver, login, personal_account, constructor):
        # Нажми кнопку «Соусы»
        driver.find_element(*StellarBurgersLocators.SAUSE).click()
        # Найди заголовок, получи его текст и проверь, что он равен 'Соусы'
        assert driver.find_element(*StellarBurgersLocators.SAUSE).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


    def test_stellar_burgers_constructor_go_to_fillings(self, driver, login, personal_account, constructor):
        # Нажми кнопку «Начинки»
        driver.find_element(*StellarBurgersLocators.FILLINGS).click()
        # Найди заголовок, получи его текст и проверь, что он равен 'Начинки'
        assert driver.find_element(*StellarBurgersLocators.FILLINGS).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
