import pytest
from selene.support.shared import browser
from selene import be, have
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def config_chrome():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    return options


@pytest.fixture(scope="session")
def open_browser():
    browser.open('https://google.com')


