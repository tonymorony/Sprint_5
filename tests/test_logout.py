from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import TestLocators


class TestLogout:

    def test_logout(self, chrome_browser):
        start_page_url = 'https://stellarburgers.nomoreparties.site/'
        login_page_url = 'https://stellarburgers.nomoreparties.site/login'
        profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'

        # Сначала нужно залогиниться
        chrome_browser.get(start_page_url)
        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(start_page_url))
        assert chrome_browser.current_url == login_page_url

        # Находим и заполняем поле "Email"
        chrome_browser.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys("testlysakov5@gmail.com")
        # Находим и заполняем поле "Пароль"
        chrome_browser.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys("123456")

        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(login_page_url))
        assert chrome_browser.current_url == start_page_url

        # Затем перейти в личный кабинет
        chrome_browser.find_element(*TestLocators.DASHBOARD_LINK).click()
        WebDriverWait(chrome_browser, 30).until(EC.presence_of_element_located(TestLocators.LOGOUT_BUTTON))
        assert chrome_browser.current_url == profile_page_url

        # Затем нажать на кнопку Выход
        chrome_browser.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(profile_page_url))
        assert chrome_browser.current_url == login_page_url
