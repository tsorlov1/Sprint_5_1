from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    NAME_FIELD_REGISTRATION = (By.XPATH, "(//input[@name='name'])[1]")  # Поле "Имя" на странице регистрации
    EMAIL_FIELD_REGISTRATION = (By.XPATH, "(//input[@name='name'])[2]")  # Поле "Email" на странице регистрации
    PASSWORD_FIELD = (By.NAME, "Пароль")  # Поле "Пароль" на странице регистрации
    BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]")  # Кнопка "Зарегистрироваться"/"Войти"
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")  # Заголовок "Войти"
    PASSWORD_ERROR_REGISTRATION = (By.XPATH, "//fieldset[3]/div/p")  # Ошибка при вводе некорректного пароля
    EMAIL_FIELD_LOGIN = (By.NAME, "name")  # Поле "Имя" на странице авторизации
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "(//p[contains(@class, 'AppHeader_header')])[3]")  # Кнопка "Личный кабинет"
    BUTTON_LOGIN_REGISTRATION_FORM = (By.XPATH, "//a[@class='Auth_link__1fOlj']")  # Кнопка "Войти" на странице регистрации
    BUTTON_PASSWORD_RECOVERY = (By.XPATH, "(//a[@class='Auth_link__1fOlj'])[2]")  # Кнопка "Восстановить пароль"
    PASSWORD_RECOVERY_PAGE = (By.XPATH, "//div[@class='Auth_login__3hAey']/h2")  # Страница восстановления пароля
    BUTTON_LOGIN = (By.XPATH, "//a[@class='Auth_link__1fOlj']")  # Кнопка "Войти" на странице восстановления пароля
    BUTTON_PROFILE = (By.XPATH, "(//a[contains(@class, 'Account_link__2ETsJ')])[1]")  # Кнопка "Профиль"
    BUTTON_EXIT = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3')]")  # Кнопка "Выход"
    BUTTON_CONSTRUCTOR = (By.XPATH, "(//p[contains(@class, 'AppHeader_header')])[1]")  # Кнопка "Конструктор"
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1")  # Заголовок "Собери свой бургер"
    FILLINGS = (By.XPATH, "(//div[contains(@class, 'tab_tab__1SPyG')])[3]")  # Начинки
    BREAD = (By.XPATH, "(//div[contains(@class, 'tab_tab__1SPyG')])[1]")  # Булки
    SAUSE = (By.XPATH, "(//div[contains(@class, 'tab_tab__1SPyG')])[2]")  # Соусы
    TITLE_BREAD = (By.XPATH, "(// h2[contains( @class , 'text')])[1]")  # Заголовок "Булки"
    TITLE_SAUSE = (By.XPATH, "(// h2[contains( @class , 'text')])[2]")  # Заголовок "Соусы"
    TITLE_FILLINGS = (By.XPATH, "(// h2[contains( @class , 'text')])[3]")  # Заголовок "Начинки"
