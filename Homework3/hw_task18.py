# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Введите количество элементов в массиве: '))
arr = list(map(int, input('Введите элементы массива через пробел: ').split()))
x = int(input('Введите число, для которого нужно найти ближайший элемент в массиве: '))
min_diff = float('inf')
closest_index = None
for i in range(n):
    diff = abs(arr[i] - x)
    if diff < min_diff:
        min_diff = diff
        closest_index = i
print(f'Ближайший элемент к заданному числу: {arr[closest_index]}')
