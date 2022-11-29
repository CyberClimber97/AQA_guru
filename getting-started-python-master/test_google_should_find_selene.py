from selene.support.shared import browser
from selene import be, have


def test_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests'))


def test_bad_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('фывфывц324124цвыа').press_enter()
    browser.element('[id=search]').should(have.text('Your search - фывфывц324124цвыа - did not match any documents'))


