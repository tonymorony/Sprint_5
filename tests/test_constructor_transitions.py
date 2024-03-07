from utils.locators import TestLocators
from utils.data import PagesURL


class TestConstructorTransitions:

    def test_constructor_transition_to_sauces_section(self, chrome_browser):
        chrome_browser.get(PagesURL.home_page_url)

        # сначала проверяю что секция неактивна перед тестом
        section_before_click = chrome_browser.find_element(*TestLocators.SAUCES_SECTION)
        class_before_click = section_before_click.get_attribute('class')
        assert 'current' not in class_before_click

        # потом кликаю и проверяю что класс изменился
        chrome_browser.find_element(*TestLocators.SAUCES_SECTION).click()
        section_after_click = chrome_browser.find_element(*TestLocators.SAUCES_SECTION)
        class_after_click = section_after_click.get_attribute('class')
        assert 'current' in class_after_click

    def test_constructor_transition_to_toppings_section(self, chrome_browser):
        chrome_browser.get(PagesURL.home_page_url)

        # сначала проверяю что секция неактивна перед тестом
        section_before_click = chrome_browser.find_element(*TestLocators.TOPPINGS_SECTION)
        class_before_click = section_before_click.get_attribute('class')
        assert 'current' not in class_before_click

        # потом кликаю и проверяю что класс изменился
        chrome_browser.find_element(*TestLocators.TOPPINGS_SECTION).click()
        section_after_click = chrome_browser.find_element(*TestLocators.TOPPINGS_SECTION)
        class_after_click = section_after_click.get_attribute('class')
        assert 'current' in class_after_click

    def test_constructor_transition_to_buns_section(self, chrome_browser):
        chrome_browser.get(PagesURL.home_page_url)

        # перехожу на другую секцию т.к. секция Булки активна по умолчанию
        chrome_browser.find_element(*TestLocators.SAUCES_SECTION).click()
        # проверяю что секция неактивна перед тестом
        section_before_click = chrome_browser.find_element(*TestLocators.BUNS_SECTION)
        class_before_click = section_before_click.get_attribute('class')
        assert 'current' not in class_before_click

        # потом кликаю и проверяю что класс изменился
        chrome_browser.find_element(*TestLocators.BUNS_SECTION).click()
        section_after_click = chrome_browser.find_element(*TestLocators.BUNS_SECTION)
        class_after_click = section_after_click.get_attribute('class')
        assert 'current' in class_after_click
