import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration_valid_data_success(generate_email, generate_valid_password):
    driver = webdriver.Chrome()

    driver.get('https://stellarburgers.nomoreparties.site/register')

    # Находим и заполняем поле "Имя"
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Антон")

    # Находим и заполняем поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(generate_email)

    # Находим и заполняем поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(generate_valid_password)

    # Кликаем на кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, "//*[contains(text(), 'Зарегистрироваться')]").click()

    WebDriverWait(driver, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/register'))

    # При успешной регистрации приложение переходит на страницу логина
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()


def test_registration_short_password_show_error(generate_email):
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Находим и заполняем поле "Имя"
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Антон")

    # Находим и заполняем поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(generate_email)

    # Находим и заполняем поле "Пароль" паролем менее минимальной длины в 6 символов
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys('pwd')

    # Кликаем на кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, "//*[contains(text(), 'Зарегистрироваться')]").click()

    # Проверяем что появилась ошибка валидации поля пароль с текстом "Некорректный пароль"
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(), 'Некорректный пароль')]")
        assert element is not None, "Element not found"
    except AssertionError as e:
        pytest.fail(str(e))

    driver.quit()
