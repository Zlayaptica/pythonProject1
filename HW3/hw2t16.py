# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
inc = 0
input('Ведите число: ')
lst = map(int, (input('Введите числа через пробел: ').split()))
n = int(input('Введите число: '))
for i in lst:
    if i == n:
        inc += 1
print(inc)