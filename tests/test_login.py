from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import TestLocators
from utils.data import PagesURL, LoginData


class TestLogin:

    def test_successful_login_main_page_enter_account_button(self, chrome_browser):
        chrome_browser.get(PagesURL.home_page_url)

        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.home_page_url))
        assert chrome_browser.current_url == PagesURL.login_page_url

        # Находим и заполняем поле "Email"
        chrome_browser.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(LoginData.email)
        # Находим и заполняем поле "Пароль"
        chrome_browser.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(LoginData.password)
        # Нажимаем на кнопку "Войти"
        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.login_page_url))
        assert chrome_browser.current_url == PagesURL.home_page_url

    def test_successful_login_main_page_dashboard_link(self, chrome_browser):
        chrome_browser.get(PagesURL.home_page_url)

        chrome_browser.find_element(*TestLocators.DASHBOARD_LINK).click()

        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.home_page_url))
        assert chrome_browser.current_url == PagesURL.login_page_url

        # Находим и заполняем поле "Email"
        chrome_browser.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(LoginData.email)
        # Находим и заполняем поле "Пароль"
        chrome_browser.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(LoginData.password)
        # Нажимаем на кнопку "Войти"
        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.login_page_url))
        assert chrome_browser.current_url == PagesURL.home_page_url

    def test_successful_login_registration_page_button(self, chrome_browser):
        chrome_browser.get(PagesURL.registration_page_url)
        chrome_browser.find_element(*TestLocators.LOGIN_LINK).click()

        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.registration_page_url))
        assert chrome_browser.current_url == PagesURL.login_page_url

        # Находим и заполняем поле "Email"
        chrome_browser.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(LoginData.email)
        # Находим и заполняем поле "Пароль"
        chrome_browser.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(LoginData.password)
        # Нажимаем на кнопку "Войти"
        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.login_page_url))
        assert chrome_browser.current_url == PagesURL.home_page_url

    def test_successful_forgot_password_page_button(self, chrome_browser):
        chrome_browser.get(PagesURL.forgot_password_page_url)
        chrome_browser.find_element(*TestLocators.LOGIN_LINK).click()

        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.forgot_password_page_url))
        assert chrome_browser.current_url == PagesURL.login_page_url

        # Находим и заполняем поле "Email"
        chrome_browser.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(LoginData.email)
        # Находим и заполняем поле "Пароль"
        chrome_browser.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(LoginData.password)
        # Нажимаем на кнопку "Войти"
        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.login_page_url))
        assert chrome_browser.current_url == PagesURL.home_page_url
