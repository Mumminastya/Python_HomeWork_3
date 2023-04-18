# 16.Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint
import sys

n = int(input('Введите N '))
x = int(input('Введите X '))
counter = 0
a=[]
for i in range(n):
    a.append(randint(0, 10))
    sys.stdout.write(f'{a[i]} ')

for i in range(n):
    if (a[i] == x):
        counter = counter + 1

print()
print(counter)