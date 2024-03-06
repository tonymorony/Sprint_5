from selenium.webdriver.common.by import By


class TestLocators:

    # Поля ввода
    NAME_INPUT_FIELD = By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input"
    EMAIL_INPUT_FIELD = By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input"
    PASSWORD_INPUT_FIELD = By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input"

    # Кнопки
    REGISTER_BUTTON = By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(), 'Войти')]"
    LOGOUT_BUTTON = By.XPATH, "//button[contains(text(), 'Выход')]"

    # Ссылки
    DASHBOARD_LINK = By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/account']"
    CONSTRUCTOR_LINK = By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/']"
    LOGIN_LINK = By.XPATH, "//a[contains(text(), 'Войти')]"
    BURGER_LOGOTYPE_LINK = By.XPATH, "//div[(@class = 'AppHeader_header__logo__2D0X2')]/following-sibling::a"

    # Разделы конструктора
    SAUCES_SECTION = By.XPATH, "//span[(@class = 'text text_type_main-default' and text()='Соусы')]/parent::div"
    BUNS_SECTION = By.XPATH, "//span[(@class = 'text text_type_main-default' and text()='Начинки')]/parent::div"
    TOPPINGS_SECTION = By.XPATH, "//span[(@class = 'text text_type_main-default' and text()='Булки')]/parent::div"

    # Ошибки
    NOT_VALID_PASSWORD_ERROR = By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"
