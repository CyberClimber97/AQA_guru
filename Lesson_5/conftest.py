import pytest
from selene import browser, have, be
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def test_complete_todo():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')              #не понял. Вроде как для выполнения в контейнере под капотом. Увеличивает скорость выполнения
    # browser.driver.maximize_window()  плохая практика
    browser.config.window_width = 1700
    browser.config.window_height = 1000
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
