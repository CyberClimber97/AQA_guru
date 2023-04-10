

# [id*=login__username] [class~=ng-pristine] //Поиск по id, class.
# (*) часть тескта в id должна быть именно такой.
# ~ поиск по форме, отделённой пробелами
# [class~=ng-pristine] === .ng-pristine  (Существует такое сокращение)

#type = напечатать
#set_value = стереть старую зпись, написать новую
#Alt+shift+E выполнить выделенную строчку

from selene import browser, have, be


# def test_successful_login():
#     browser.open('http://192.168.150.11/#/login')
#     browser.element('.ng-pristine [id*=login__username]').type('yakovlev')
#     browser.element('[id*=login__password]').set_value('Bazalt1!').press_enter()
#
#     browser.element(('.header-logo header-link header-tree ng-tns-c402-41 ng-star-inserted clicked-link'))
#     browser.should(have.url('http://192.168.150.11/#/pages/main'))
#     #browser.element('.ng-tns-c402-11').should(have.text('yakovlev'))

def test_successful_login():
    browser.open('https://qa.guru/cms/system/login')
    browser.element('.form-field-email').type('form-field-email')
    browser.element('[id*=login__password]').set_value('Bazalt1!').press_enter()
    #
    browser.element((''))
    browser.should(have.url(''))
    browser.element('').should(have.text('yakovlev'))
