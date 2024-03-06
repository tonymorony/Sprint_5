from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import TestLocators


class TestTransitions:

    def test_transition_to_personal_dashboard_when_login(self, chrome_browser):
        home_page_url = 'https://stellarburgers.nomoreparties.site/'
        login_page_url = 'https://stellarburgers.nomoreparties.site/login'
        profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'

        # Сначала нужно залогиниться
        chrome_browser.get(home_page_url)
        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
        assert chrome_browser.current_url == login_page_url

        # Находим и заполняем поле "Email"
        chrome_browser.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys("testlysakov5@gmail.com")
        # Находим и заполняем поле "Пароль"
        chrome_browser.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys("123456")

        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(login_page_url))
        assert chrome_browser.current_url == home_page_url

        # Затем переходим в личный кабинет
        chrome_browser.find_element(*TestLocators.DASHBOARD_LINK).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
        assert chrome_browser.current_url == profile_page_url

    def test_transition_from_personal_dashboard_to_constructor_click_on_href(self, chrome_browser):
        home_page_url = 'https://stellarburgers.nomoreparties.site/'
        login_page_url = 'https://stellarburgers.nomoreparties.site/login'
        profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'

        # Сначала нужно залогиниться
        chrome_browser.get(home_page_url)
        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
        assert chrome_browser.current_url == login_page_url

        # Находим и заполняем поле "Email"
        chrome_browser.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys("testlysakov5@gmail.com")
        # Находим и заполняем поле "Пароль"
        chrome_browser.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys("123456")

        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(login_page_url))
        assert chrome_browser.current_url == home_page_url

        # Затем переходим в личный кабинет
        chrome_browser.find_element(*TestLocators.DASHBOARD_LINK).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
        assert chrome_browser.current_url == profile_page_url

        # Затем кликаем на конструктор
        chrome_browser.find_element(*TestLocators.CONSTRUCTOR_LINK).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(profile_page_url))
        assert chrome_browser.current_url == home_page_url

    def test_transition_from_personal_dashboard_to_constructor_click_on_logo(self, chrome_browser):
        home_page_url = 'https://stellarburgers.nomoreparties.site/'
        login_page_url = 'https://stellarburgers.nomoreparties.site/login'
        profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'

        # Сначала нужно залогиниться
        chrome_browser.get(home_page_url)
        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
        assert chrome_browser.current_url == login_page_url

        # Находим и заполняем поле "Email"
        chrome_browser.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys("testlysakov5@gmail.com")
        # Находим и заполняем поле "Пароль"
        chrome_browser.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys("123456")

        chrome_browser.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(login_page_url))
        assert chrome_browser.current_url == home_page_url

        # Затем переходим в личный кабинет
        chrome_browser.find_element(*TestLocators.DASHBOARD_LINK).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
        assert chrome_browser.current_url == profile_page_url

        # Затем кликаем на логотип
        chrome_browser.find_element(*TestLocators.BURGER_LOGOTYPE_LINK).click()
        WebDriverWait(chrome_browser, 30).until(EC.url_changes(profile_page_url))
        assert chrome_browser.current_url == home_page_url

    def test_constructor_transition_to_sauces_section(self, chrome_browser):
        home_page_url = 'https://stellarburgers.nomoreparties.site/'
        chrome_browser.get(home_page_url)

        chrome_browser.find_element(*TestLocators.SAUCES_SECTION).click()

        # TODO: fix me
        pass

    def test_constructor_transition_to_toppings_section(self, chrome_browser):
        home_page_url = 'https://stellarburgers.nomoreparties.site/'
        chrome_browser.get(home_page_url)

        chrome_browser.find_element(*TestLocators.TOPPINGS_SECTION).click()

        # TODO: fix me
        pass

    def test_constructor_transition_to_buns_section(self, chrome_browser):
        home_page_url = 'https://stellarburgers.nomoreparties.site/'
        chrome_browser.get(home_page_url)

        # после клика заголовок "Булки" должен отображаться сразу под меню
        # т.к. это дефолтное состояние, сначала переходим в другую секцию
        chrome_browser.find_element(*TestLocators.SAUCES_SECTION).click()

        chrome_browser.find_element(*TestLocators.BUNS_SECTION).click()
        # TODO: fix me
        pass
