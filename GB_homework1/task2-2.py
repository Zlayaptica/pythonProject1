#Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |


n = input('Введите целое положительное число: ')
print(int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2]))