import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.login_data_generators import generate_email, generate_valid_password
from utils.locators import TestLocators
from utils.data import PagesURL, LoginData


class TestRegistration:

    def test_registration_valid_data_success(self, chrome_browser):
        chrome_browser.get(PagesURL.registration_page_url)

        # Находим и заполняем поле "Имя"
        chrome_browser.find_element(*TestLocators.NAME_INPUT_FIELD).send_keys(LoginData.name)
        # Находим и заполняем поле "Email"
        chrome_browser.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(generate_email())
        # Находим и заполняем поле "Пароль"
        chrome_browser.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(generate_valid_password())
        # Кликаем на кнопку "Зарегистрироваться"
        chrome_browser.find_element(*TestLocators.REGISTER_BUTTON).click()

        WebDriverWait(chrome_browser, 30).until(EC.url_changes(PagesURL.registration_page_url))

        # При успешной регистрации приложение переходит на страницу логина
        assert chrome_browser.current_url == PagesURL.login_page_url

    def test_registration_short_password_show_error(self, chrome_browser):
        chrome_browser.get(PagesURL.registration_page_url)

        # Находим и заполняем поле "Имя"
        chrome_browser.find_element(*TestLocators.NAME_INPUT_FIELD).send_keys(LoginData.name)
        # Находим и заполняем поле "Email"
        chrome_browser.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(generate_email())
        # Находим и заполняем поле "Пароль" паролем менее минимальной длины в 6 символов
        chrome_browser.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(LoginData.short_password)
        # Кликаем на кнопку "Зарегистрироваться"
        chrome_browser.find_element(*TestLocators.REGISTER_BUTTON).click()

        # Проверяем что появилась ошибка валидации поля пароль с текстом "Некорректный пароль"
        try:
            element = chrome_browser.find_element(*TestLocators.NOT_VALID_PASSWORD_ERROR)
            assert element is not None, "Element not found"
        except AssertionError as e:
            pytest.fail(str(e))
