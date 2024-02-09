from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login_main_page_enter_account_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.XPATH, "//*[contains(text(), 'Войти в аккаунт')]").click()

    WebDriverWait(driver, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # Находим и заполняем поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(driver, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()


def test_successful_login_main_page_personal_area_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.XPATH, "//*[contains(text(), 'Личный Кабинет')]").click()

    WebDriverWait(driver, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # Находим и заполняем поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(driver, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()


def test_successful_login_registration_page_button():
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(driver, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/register'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # Находим и заполняем поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(driver, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()


def test_successful_forgot_password_page_button():
    driver = webdriver.Chrome()

    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
    driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(driver, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/forgot-password'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # Находим и заполняем поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()

    WebDriverWait(driver, 30).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()
