from time import time

from selene import browser, have, be


def test_complete_todo():
    browser.open("/")                #Можно дописать URL если нужно в следующей вкладке

    browser.element('#firstName').should(have.value(''))
    browser.element('#firstName').set_value('Yakovlev')             #.press_enter() set_value() = clear().type()
    browser.element('#lastName').should(be.blank)                   # should(be.blank) == should(have.value(''))
    browser.element('#lastName').type('Dmitry')
    browser.element('#gender-radio-1').click()
    browser.element('#userNumber').set_value('88888888888')
    browser.element('#submit').click()


    #browser.all('#todo-list li').element_by(have.exact_text('b')).element('.toggle').click()            #Находим конкретный элемент списка. Затем конкретный элемент по классу toggle (чекбокс) и кликаем
    # Также в данном случае ".element_by(have.exact_text('b'))" == .second
    # browser.all('#todo-list li').element_by(have.css_class('completed')).should(have.text('b'))       # Закомпличенный чекбокс имеет текст 'b'. Но это не очень хорошая проверка, т.к. закомпличенных элементов может быть больше чем 1.
    # browser.all('#todo-list li').by(have.css_class('completed')).should(have.exact_text('b'))         # Так корректно. Во всём списке комплитед задач только задача с текстом 'b'
    # browser.all('#todo-list li').by(have.no.css_class('completed')).should(have.exact_texts('a', 'c'))    #Проверка для не закомпличенных элементов

    #browser.element('#gender-radio-1')
    #browser.all('#todo-list li').should(have.size(3))           #Количесво элементов в списке равно 3
    # browser.all('#todo-list li')[0].should(have.exact_text('a'))  #Элемент под индексом [0] имеет текст в точности 'a'. Лайфхак: [0] = first в Селене (есть еще second. Therd нет)

    #unique_todo = f'test todo {time()}'
    #browser.element('#new-todo').type(unique_todo).press_enter()         #Вместо ранодома
    # browser.all('#todo-list li').should(have.exact_texts('a', 'b', 'c'))      #Проверка что все элементы списка имеют именно такие тексты




    # browser.all('#todo-list li')[-1].should(have.exact_text('unique_todo'))     #Проверка, что в создался в конце списка элемент с unique_todo
    # browser.all('#todo-list li').element_by(have.exact_text('unique_todo')).should(be.visible)     #Проверка по всей коллекции элементов, что есть unique_todo
    # browser.all('#todo-list li').by(have.exact_text('unique_todo')).should(have.size(1))            #Проверка по всем элементам, что unique_todo в одном экземпляре в коллекции
    # browser.all('#todo-list li').by(have.text('unique_todo')).should(have.size(1))            #Та же, что и выше, только не по точному сравнению. Может быть и другой текст, кроме unique_todo


 #   browser.should()
