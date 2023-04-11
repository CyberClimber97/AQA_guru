

# [id*=login__username] [class~=ng-pristine] //Поиск по id, class.
# (*) часть тескта в id должна быть именно такой.
# ~ поиск по форме, отделённой пробелами
# [class~=ng-pristine] === .ng-pristine  (Существует такое сокращение)

#type = напечатать
#set_value = стереть старую зпись, написать новую
#Alt+shift+E выполнить выделенную строчку

# from selene import browser, have, be


# def test_successful_login():
#     browser.open('http://192.168.150.11/#/login')
#     browser.element('.ng-pristine [id*=login__username]').type('yakovlev')
#     browser.element('[id*=login__password]').set_value('Bazalt1!').press_enter()
#
#     browser.element(('.header-logo header-link header-tree ng-tns-c402-41 ng-star-inserted clicked-link'))
#     browser.should(have.url('http://192.168.150.11/#/pages/main'))
#     #browser.element('.ng-tns-c402-11').should(have.text('yakovlev'))

# def test_successful_login():
#     browser.open('https://qa.guru/cms/system/login')
#     browser.element('.form-field-email [name=email] ').type('dmitry97yakovlev@mail.ru')
#     browser.element('[name=password]').set_value('qwerty').press_enter()
#
#     browser.element('.content-1920').click()
#     browser.should(have.url('https://qa.guru/'))
#     # browser.element('[class=title]').should(have.text('Школа инженеров по автоматизации тестирования на Java'))
import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def size_window():
    browser.open('https://google.com')
    browser.driver.set_window_size(1920, 1080)


@pytest.fixture
def open_browser(size_window):
    browser.open('https://google.com')


def test_successful_login(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))