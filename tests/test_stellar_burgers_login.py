from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL, EMAIL, PASSWORD
from locators import StellarBurgersLocators


class Test_Stellar_Burgers_Login:
    def test_stellar_burgers_successful_login(self, driver):
        # Открой страницу https://stellarburgers.nomoreparties.site/login
        driver.get(f'{URL}login')
        # Выполни авторизацию
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOGIN).send_keys(EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(*StellarBurgersLocators.BUTTON).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.BUTTON_ORDER))
        # Проверь, что появилась кнопка 'Оформить заказ'
        assert driver.find_element(*StellarBurgersLocators.BUTTON_ORDER).text == 'Оформить заказ'


    def test_stellar_burgers_login_button_log_account(self, driver):
        # Нажми кнопку «Войти в аккаунт»
        driver.find_element(*StellarBurgersLocators.BUTTON).click()
        # Добавь явное ожидание для загрузки страницы авторизации
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))
        # Проверь, что текущий url равен https://stellarburgers.nomoreparties.site/login
        assert driver.current_url == f'{URL}login'


    def test_stellar_burgers_login_button_personal_account(self, driver):
        # Нажми кнопку «Личный кабинет»
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        # Добавь явное ожидание для загрузки страницы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))
        # Проверь, что текущий url равен https://stellarburgers.nomoreparties.site/login
        assert driver.current_url == f'{URL}login'


    def test_stellar_burgers_login_button_registration_form(self, driver):
        driver.get(f'{URL}register')
        # Нажми кнопку «Войти»
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_REGISTRATION_FORM).click()
        # Добавь явное ожидание для загрузки страницы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))
        # Проверь, что текущий url равен https://stellarburgers.nomoreparties.site/login
        assert driver.current_url == f'{URL}login'


    def test_stellar_burgers_login_password_recovery_personal_account(self, driver):
        # Нажми кнопку «Личный кабинет»
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        # Добавь явное ожидание для загрузки страницы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))
        # Нажми кнопку «Восстановление пароля»
        driver.find_element(*StellarBurgersLocators.BUTTON_PASSWORD_RECOVERY).click()
        # Добавь явное ожидание для загрузки страницы «Восстановление пароля»
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.PASSWORD_RECOVERY_PAGE))
        # Нажми кнопку «Войти»
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN).click()
        # Добавь явное ожидание для загрузки страницы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))
        # Проверь, что текущий url равен https://stellarburgers.nomoreparties.site/login
        assert driver.current_url == f'{URL}login'


    def test_stellar_burgers_login_password_recovery_log_account(self, driver):
        # Нажми кнопку «Войти в аккаунт»
        driver.find_element(*StellarBurgersLocators.BUTTON).click()
        # Добавь явное ожидание для загрузки страницы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))
        # Нажми кнопку «Восстановление пароля»
        driver.find_element(*StellarBurgersLocators.BUTTON_PASSWORD_RECOVERY).click()
        # Добавь явное ожидание для загрузки страницы «Восстановление пароля»
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.PASSWORD_RECOVERY_PAGE))
        # Нажми кнопку «Войти»
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN).click()
        # Добавь явное ожидание для загрузки страницы авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))
        # Проверь, что текущий url равен https://stellarburgers.nomoreparties.site/login
        assert driver.current_url == f'{URL}login'
