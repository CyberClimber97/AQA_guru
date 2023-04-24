from selene import browser, have
import os


def test_demo_form(browser_open):
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Dima')
    browser.element('#lastName').type('Yak')
    browser.element('#userEmail').type('a@a.aa')
    browser.element('[for = gender-radio-1]').double_click()
    browser.element('#userNumber').type('9009002020')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="2000"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="8"]').click()
    browser.element('[aria-label="Choose Friday, September 8th, 2000"]').click()

    browser.element('#subjectsInput').type('IT').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/resources/cat_internet.jpg')

    browser.element('#currentAddress').type('Moscow city')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.texts(
        'Student Name Dima Yak', 'Student Email a@a.aa', 'Gender Male', 'Mobile 9009002020',
        'Date of Birth 08 September,2000', 'Subjects IT', 'Hobbies Reading', 'Picture cat_internet.jpg',
        'Address Moscow city', 'State and City NCR Delhi'))