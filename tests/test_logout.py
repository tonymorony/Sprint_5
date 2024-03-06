from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import TestLocators
from utils.data import PagesURL, LoginData


class TestLogout:

    def test_logout(self, chrome_browser):
        # Сначала нужно залогиниться
        chrome_browser.get(PagesURL.home_page_url)
        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.home_page_url))
        assert chrome_browser.current_url == PagesURL.login_page_url

        # Находим и заполняем поле "Email"
        chrome_browser.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(LoginData.email)
        # Находим и заполняем поле "Пароль"
        chrome_browser.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(LoginData.password)

        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.login_page_url))
        assert chrome_browser.current_url == PagesURL.home_page_url

        # Затем перейти в личный кабинет
        chrome_browser.find_element(*TestLocators.DASHBOARD_LINK).click()
        WebDriverWait(chrome_browser, 30).until(EC.presence_of_element_located(TestLocators.LOGOUT_BUTTON))
        assert chrome_browser.current_url == PagesURL.profile_page_url

        # Затем нажать на кнопку Выход
        chrome_browser.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.profile_page_url))
        assert chrome_browser.current_url == PagesURL.login_page_url
