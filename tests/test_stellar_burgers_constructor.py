from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import StellarBurgersLocators


class Test_Stellar_Burgers_Constructor:
    def test_stellar_burgers_constructor_go_to_bread(self, driver):
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
        # Добавь явное ожидание для загрузки страницы Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.BUTTON_PROFILE))
        # Нажми кнопку «Конструктор»
        driver.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCTOR).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_TITLE))
        # Нажми кнопку «Начинки»
        driver.find_element(*StellarBurgersLocators.FILLINGS).click()
        # Нажми кнопку «Булки»
        driver.find_element(*StellarBurgersLocators.BREAD).click()
        # Найди заголовок, получи его текст и проверь, что он равен 'Булки'
        assert driver.find_element(*StellarBurgersLocators.TITLE_BREAD).text == 'Булки'


    def test_stellar_burgers_constructor_go_to_fillings(self, driver):
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
        # Добавь явное ожидание для загрузки страницы Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.BUTTON_PROFILE))
        # Нажми кнопку «Конструктор»
        driver.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCTOR).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_TITLE))
        # Нажми кнопку «Соусы»
        driver.find_element(*StellarBurgersLocators.SAUSE).click()
        # Найди заголовок, получи его текст и проверь, что он равен 'Соусы'
        assert driver.find_element(*StellarBurgersLocators.TITLE_SAUSE).text == 'Соусы'


    def test_stellar_burgers_constructor_go_to_fillings(self, driver):
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
        # Добавь явное ожидание для загрузки страницы Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.BUTTON_PROFILE))
        # Нажми кнопку «Конструктор»
        driver.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCTOR).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_TITLE))
        # Нажми кнопку «Начинки»
        driver.find_element(*StellarBurgersLocators.FILLINGS).click()
        # Найди заголовок, получи его текст и проверь, что он равен 'Начинки'
        assert driver.find_element(*StellarBurgersLocators.TITLE_FILLINGS).text == 'Начинки'
