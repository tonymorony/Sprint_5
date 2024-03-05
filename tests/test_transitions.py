from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_transition_to_personal_dashboard_when_login(chrome_browser):
    home_page_url = 'https://stellarburgers.nomoreparties.site/'
    login_page_url = 'https://stellarburgers.nomoreparties.site/login'
    profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'

    # Сначала нужно залогиниться
    chrome_browser.get(home_page_url)
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти в аккаунт')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
    assert chrome_browser.current_url == login_page_url

    # Находим и заполняем поле "Email"
    chrome_browser.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    chrome_browser.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(login_page_url))
    assert chrome_browser.current_url == home_page_url

    # Затем переходим в личный кабинет
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Личный Кабинет')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
    assert chrome_browser.current_url == profile_page_url


def test_transition_from_personal_dashboard_to_constructor_click_on_href(chrome_browser):
    home_page_url = 'https://stellarburgers.nomoreparties.site/'
    login_page_url = 'https://stellarburgers.nomoreparties.site/login'
    profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'

    # Сначала нужно залогиниться
    chrome_browser.get(home_page_url)
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти в аккаунт')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
    assert chrome_browser.current_url == login_page_url

    # Находим и заполняем поле "Email"
    chrome_browser.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    chrome_browser.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(login_page_url))
    assert chrome_browser.current_url == home_page_url

    # Затем переходим в личный кабинет
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Личный Кабинет')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
    assert chrome_browser.current_url == profile_page_url

    # Затем кликаем на конструктор
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Конструктор')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(profile_page_url))
    assert chrome_browser.current_url == home_page_url


def test_transition_from_personal_dashboard_to_constructor_click_on_logo(chrome_browser):
    home_page_url = 'https://stellarburgers.nomoreparties.site/'
    login_page_url = 'https://stellarburgers.nomoreparties.site/login'
    profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'

    # Сначала нужно залогиниться
    chrome_browser.get(home_page_url)
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти в аккаунт')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
    assert chrome_browser.current_url == login_page_url

    # Находим и заполняем поле "Email"
    chrome_browser.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("testlysakov5@gmail.com")
    # Находим и заполняем поле "Пароль"
    chrome_browser.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("123456")

    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Войти')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(login_page_url))
    assert chrome_browser.current_url == home_page_url

    # Затем  в личный кабинет
    chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Личный Кабинет')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(home_page_url))
    assert chrome_browser.current_url == profile_page_url

    # Затем кликаем на логотип
    chrome_browser.find_element(By.XPATH, "//*[(@class = 'AppHeader_header__logo__2D0X2')]").click()
    WebDriverWait(chrome_browser, 30).until(EC.url_changes(profile_page_url))
    assert chrome_browser.current_url == home_page_url


def test_constructor_transition_to_sauces_section(chrome_browser):
    home_page_url = 'https://stellarburgers.nomoreparties.site/'
    chrome_browser.get(home_page_url)

    chrome_browser.find_element(By.XPATH, "//*[(@class = 'text text_type_main-default' and text()='Соусы')]").click()

    menu_element = chrome_browser.find_element(By.XPATH, "//*[(@class = 'text text_type_main-default' and text()='Соусы')]")
    sauces_section_header = chrome_browser.find_element(By.XPATH, ".//h2[text()='Соусы']")

    menu_position = menu_element.location['y']
    sauces_position = sauces_section_header.location['y']

    # после клика заголовок "Cоусы" должен отображаться под меню
    assert sauces_position > menu_position


def test_constructor_transition_to_toppings_section(chrome_browser):
    home_page_url = 'https://stellarburgers.nomoreparties.site/'
    chrome_browser.get(home_page_url)

    chrome_browser.find_element(By.XPATH, "//*[(@class = 'text text_type_main-default' and text()='Начинки')]").click()

    menu_element = chrome_browser.find_element(By.XPATH, "//*[(@class = 'text text_type_main-default' and text()='Начинки')]")
    toppings_section_header = chrome_browser.find_element(By.XPATH, ".//h2[text()='Начинки']")

    menu_position = menu_element.location['y']
    toppings_position = toppings_section_header.location['y']

    # после клика заголовок "Начинки" должен отображаться сразу под меню
    assert toppings_position > menu_position


def test_constructor_transition_to_buns_section(chrome_browser):
    home_page_url = 'https://stellarburgers.nomoreparties.site/'
    chrome_browser.get(home_page_url)

    # после клика заголовок "Булки" должен отображаться сразу под меню
    # т.к. это дефолтное состояние, сначала переходим в другую секцию
    chrome_browser.find_element(By.XPATH, "//*[(@class = 'text text_type_main-default' and text()='Соусы')]").click()
    WebDriverWait(chrome_browser, 1)
    chrome_browser.find_element(By.XPATH, "//*[(@class = 'text text_type_main-default' and text()='Булки')]").click()
    WebDriverWait(chrome_browser, 1)
    menu_element = chrome_browser.find_element(By.XPATH, "//*[(@class = 'text text_type_main-default' and text()='Булки')]")
    buns_section_header = chrome_browser.find_element(By.XPATH, ".//h2[text()='Булки']")

    menu_position = menu_element.location['y']
    buns_position = buns_section_header.location['y']

    # после клика заголовок "Булки" должен отображаться сразу под меню
    assert buns_position > menu_position
