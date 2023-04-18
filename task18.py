# 18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X .
# Если таких значений больше одного, вывести первый найденный.

from random import randint
import sys

n = int(input('Введите N '))
x = int(input('Введите X '))
a=[]
for i in range(n):
    a.append(randint(0, 10))
    sys.stdout.write(f'{a[i]} ')

delta = -1
result = -1
for i in range(n):
    buf = abs(a[i] - x)
    if (delta == -1 or delta > buf):
        delta = buf
        result = a[i] 


print()
print(result)