import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def chrome_browser():

    driver = webdriver.Chrome()
    yield driver

    driver.quit()
