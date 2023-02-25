"""
Задание 3. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
Пример:
для списка [5, "string", 0.15, True, None]
результат
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

type_list = [5, 3/6, True, False, [1,2], "Hello", {"number": "lesson", "car": "supra"},(1,2)]
for i in range (len(type_list)) :
    print(f"Тип переменной в списке: {type(type_list[i])}")