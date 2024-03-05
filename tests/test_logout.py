from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout(chrome_browser):
    start_page_url = 'https://stellarburgers.nomoreparties.site/'
    login_page_url = 'https://stellarburgers.nomoreparties.site/login'
    profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'

    # Сначала нужно залогиниться
    chrome_browser.get(start_page_url)
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти в аккаунт')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(start_page_url))
    assert chrome_browser.current_url == login_page_url

    # Находим и заполняем поле "Email"
    chrome_browser.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    chrome_browser.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(login_page_url))
    assert chrome_browser.current_url == start_page_url

    # Затем перейти в личный кабинет
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Личный Кабинет')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(start_page_url))
    assert chrome_browser.current_url == profile_page_url

    # Затем нажать на кнопку Выход
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Выход')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(profile_page_url))
    assert chrome_browser.current_url == login_page_url
