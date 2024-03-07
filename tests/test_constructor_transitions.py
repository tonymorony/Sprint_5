from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import TestLocators
from utils.data import PagesURL
from selenium.webdriver.support import expected_conditions as EC


class TestConstructorTransitions:

    def test_constructor_transition_to_sauces_section(self, chrome_browser):
        chrome_browser.get(PagesURL.home_page_url)
        chrome_browser.find_element(*TestLocators.SAUCES_SECTION).click()
        assert WebDriverWait(chrome_browser, 30).until(
            EC.text_to_be_present_in_element_attribute(TestLocators.SAUCES_SECTION, 'class', 'current'))

    def test_constructor_transition_to_toppings_section(self, chrome_browser):
        chrome_browser.get(PagesURL.home_page_url)
        chrome_browser.find_element(*TestLocators.TOPPINGS_SECTION).click()
        assert WebDriverWait(chrome_browser, 30).until(
            EC.text_to_be_present_in_element_attribute(TestLocators.TOPPINGS_SECTION, 'class', 'current'))

    def test_constructor_transition_to_buns_section(self, chrome_browser):
        chrome_browser.get(PagesURL.home_page_url)

        # сначала перехожу на другую секцию т.к. секция Булки активна по умолчанию
        chrome_browser.find_element(*TestLocators.TOPPINGS_SECTION).click()
        # ожидаю окончания скролла, т.к. пока он не закончится нельзя перейти в другую секцию
        WebDriverWait(chrome_browser, 30).until(
            EC.text_to_be_present_in_element_attribute(TestLocators.TOPPINGS_SECTION, 'class', 'current'))

        chrome_browser.find_element(*TestLocators.BUNS_SECTION).click()
        # секция становится активной только после окончания скролла
        # при этом если идет переход через секцию то промежуточная секция становится на время активной
        assert WebDriverWait(chrome_browser, 30).until(
            EC.text_to_be_present_in_element_attribute(TestLocators.BUNS_SECTION, 'class', 'current'))
