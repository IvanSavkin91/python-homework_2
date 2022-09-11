# # Задание 5 Реализуйте алгоритм перемешивания списка.

# from typing import List

# import random
# n = int(input('Введите число N '))
# spam = list(range(-n, n+1))
# print(f'Список  от -{n} до {n} {spam}')
# for i in range(len(spam)):
#     j = random.randint(0, i + 1)    
#     spam[i], spam[j] = spam[j], spam[i]
# print(f'Список отсортированный {spam}')

from random import randint
 
n = int(input('Введите размер списка: '))
a = []
for i in range(n):
    a.append(randint(1, 150))
print(f'Первоначальный список {a}')
 
 
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
 
print(f'Отсортированный список методом пузырька {a}')