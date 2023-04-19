""" round(1.33333, 2) Округлит до 2 заноков полсе запятой
       out: 1.33
int(1.333) Округлит до 1
#####################################
h = 'hello'
w = 'world'
print(f"{h.title}, {w.upper}!")  #выведет Hello, WORLD!
print("{a}, {b}{b}{b}{b}{b}!".format(a=h, b=w))  #
##################################################
s = "1234"
n = 1234
assert int(s) == n
 assert s == str(n)
######################################################
Cписки
l = [1, 2, [3, 4, 6]]
l[-1][-1] = "a"                # Вместо 6 будет а

l[::-1}

l.append()   # Добавить элемент в конец списка
l.insert()    # Вставить новый элемент на определенных индекс списка
l.sort()     # Сортировака по возврастанию
##################################################################
Множества set()
Print(set([1, 2, 3, 4, 4, 4]))   # Выведет {1, 2, 3, 4}
print({1, 2, 3, 4} & {3, 4, 5, 6})  Выведет 3, 4
print({1, 2, 3, 4} | {3, 4, 5, 6})  Выведет 1, 2, 3, 4, 5, 6

l = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5]
print(list(set(l)))                 # set(l) - приведение списка во множество  list(set(l))) - приведение в список обратно
#######################################################################################
Словари (ключ = значение)

print(list(l.keys()))       # Выведет список всех ключей словаря
print(list(l.values()))       # Выведет список всех значений словаря
print(list(l.items()))       # Выведет весь словарь в виде ключ, значение

ll = copy(l)                        #Устраняет проблему с l = ll, где при изменении данных в одном словаре, меняются данные и во втором. Но ттолько на 1 уровне
from copy import deepcopy           #Устроняет ту же проблему, но и если есть вложенные словри и тд
ll = deepcopy()
##########################################################################################
Кортежи (заранее запрещают вносить изменения в эти структуры) Присвоение новых элементов, сортировака, переприсвоение - не работает
tuple() - кортеж
t = (1, 2, 3)           # Работает поиск по индексу и посчитать кол-во элементов
#########################################################################################
frozenset().   Это неизменяемые множества

"""

###
import math


def test_greeting():
    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    # TODO сосчитайте периметр
    perimeter = 2*a + 2*b
    assert perimeter == 60
    # TODO сосчитайте площадь
    area = a*b
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = math.pi * r**2
    assert area == 1661.9025137490005
    # TODO сосчитайте длину окружности
    length = 2 * math.pi *r
    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """
    # TODO создайте список
    from random import randint

    l = []
    for i in range(10):
        l.append(randint(0, 100))
    l.sort()
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    l = list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.  zip от слова zipper (застёжка-молния) -- сшивает половинки: первый элемент это объединение первых элементов аргументов
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))

    print(list(d.items()))
    assert isinstance(d, dict)
    assert len(d) == 5