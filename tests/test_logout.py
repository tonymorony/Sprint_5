from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout():
    driver = webdriver.Chrome()

    start_page_url = 'https://stellarburgers.nomoreparties.site/'
    login_page_url = 'https://stellarburgers.nomoreparties.site/login'
    profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'

    # Сначала нужно залогиниться
    driver.get(start_page_url)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Войти в аккаунт')]").click()
    WebDriverWait(driver, 30).until(EC.url_changes(start_page_url))
    assert driver.current_url == login_page_url

    # Находим и заполняем поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()
    WebDriverWait(driver, 30).until(EC.url_changes(login_page_url))
    assert driver.current_url == start_page_url

    # Затем перейти в личный кабинет
    driver.find_element(By.XPATH, "//*[contains(text(), 'Личный Кабинет')]").click()
    WebDriverWait(driver, 30).until(EC.url_changes(start_page_url))
    assert driver.current_url == profile_page_url

    # Затем нажать на кнопку Выход
    driver.find_element(By.XPATH, "//*[contains(text(), 'Выход')]").click()
    WebDriverWait(driver, 30).until(EC.url_changes(profile_page_url))
    assert driver.current_url == login_page_url
    driver.quit()
