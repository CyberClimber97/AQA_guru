# pip install -r requitements.txt  Установка всех зависимостей из файла requitements.txt
# .\venv\Scripts\activate.bat  Для перехода на (venv) в терминале. Использования локально созданного окружения
# в терминале: pytest .   Это запустит все тесты в проекте
# Фикстуры: функции перед и после тестов. через декоратор @pytest.fixture
# pass  Заглушка
# yield фикстура выполнится после тестов


def test_addition(user):
    a = 1 + 2
    assert a == 3 #Проверка
    assert open_browser == "Chrome"
    assert user == 123
    pass  #Заглушка