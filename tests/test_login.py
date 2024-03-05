from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login_main_page_enter_account_button(chrome_browser):
    chrome_browser.get("https://stellarburgers.nomoreparties.site")

    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти в аккаунт')]").click()

    WebDriverWait(chrome_browser, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site'))
    assert chrome_browser.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # Находим и заполняем поле "Email"
    chrome_browser.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    chrome_browser.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(chrome_browser, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
    assert chrome_browser.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_successful_login_main_page_personal_area_button(chrome_browser):
    chrome_browser.get("https://stellarburgers.nomoreparties.site")

    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Личный Кабинет')]").click()

    WebDriverWait(chrome_browser, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site'))
    assert chrome_browser.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # Находим и заполняем поле "Email"
    chrome_browser.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    chrome_browser.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(chrome_browser, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
    assert chrome_browser.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_successful_login_registration_page_button(chrome_browser):
    chrome_browser.get("https://stellarburgers.nomoreparties.site/register")
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(chrome_browser, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/register'))
    assert chrome_browser.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # Находим и заполняем поле "Email"
    chrome_browser.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    chrome_browser.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(chrome_browser, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
    assert chrome_browser.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_successful_forgot_password_page_button(chrome_browser):
    chrome_browser.get('https://stellarburgers.nomoreparties.site/forgot-password')
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(chrome_browser, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/forgot-password'))
    assert chrome_browser.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # Находим и заполняем поле "Email"
    chrome_browser.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    chrome_browser.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(chrome_browser, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
    assert chrome_browser.current_url == 'https://stellarburgers.nomoreparties.site/'
