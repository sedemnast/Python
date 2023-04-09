# Задача 26
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))

def power(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * power(a, b - 1)
    else:
        return 1 / (a * power(a, -b - 1))

result = power(a, b)
print(f'Число {a} в степени {b} равно {result}')

