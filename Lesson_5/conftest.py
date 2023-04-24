import pytest
from selene import browser, have, be
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_open():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')              #не понял. Вроде как для выполнения в контейнере под капотом. Увеличивает скорость выполнения
    # browser.driver.maximize_window()  плохая практика
    # browser.config.driver_name = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'