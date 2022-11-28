from selene.support.shared import browser
from selene import be, have


def test_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_bad_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('фывфывц324124цвыа').press_enter()
    browser.element('[id="search"]').should(have.text('По запросу фывфывц324124цвыа ничего не найдено.'))



def conflict():
    assert 0 == 0


def conflict2():
    assert 1 != 0