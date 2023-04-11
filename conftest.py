import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture(scope="session") # session - фикстура выполнится один раз. function - значение по умолчанию.
def open_browser():
    return "Chrome"


@pytest.fixture
def user(open_browser):
    #Возвращаем  UserID

    yield 123
    print('Текст после прохождения теста')


@pytest.fixture(scope="session")
def size_window():
    browser.driver.set_window_size(1920, 1080)