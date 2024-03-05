import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.login_data_generators import generate_email, generate_valid_password


def test_registration_valid_data_success(chrome_browser):
    chrome_browser.get('https://stellarburgers.nomoreparties.site/register')

    # Находим и заполняем поле "Имя"
    chrome_browser.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Антон")

    # Находим и заполняем поле "Email"
    chrome_browser.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(generate_email())

    # Находим и заполняем поле "Пароль"
    chrome_browser.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(generate_valid_password())

    # Кликаем на кнопку "Зарегистрироваться"
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Зарегистрироваться')]").click()

    WebDriverWait(chrome_browser, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/register'))

    # При успешной регистрации приложение переходит на страницу логина
    assert chrome_browser.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_registration_short_password_show_error(chrome_browser):
    chrome_browser.get("https://stellarburgers.nomoreparties.site/register")

    # Находим и заполняем поле "Имя"
    chrome_browser.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Антон")

    # Находим и заполняем поле "Email"
    chrome_browser.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(generate_email())

    # Находим и заполняем поле "Пароль" паролем менее минимальной длины в 6 символов
    chrome_browser.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys('pwd')

    # Кликаем на кнопку "Зарегистрироваться"
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Зарегистрироваться')]").click()

    # Проверяем что появилась ошибка валидации поля пароль с текстом "Некорректный пароль"
    try:
        element = chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Некорректный пароль')]")
        assert element is not None, "Element not found"
    except AssertionError as e:
        pytest.fail(str(e))
