# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

n = int(input('Введите количество монет: '))
heads = tails = 0
print(f'Введите {n} раз любое из значений: 0 (герб) или 1 (решка).')
for i in range(n):
    x = int(input())
    if x == 0:
        heads += 1
    else:
        tails += 1
if tails > heads:
    print(f'Нужно перевернуть столько монет: {heads}, чтобы они все были повернуты решкой вверх.')
else:
    print(f'Нужно перевернуть столько монет: {tails}, чтобы они все были повернуты гербом вверх.')
