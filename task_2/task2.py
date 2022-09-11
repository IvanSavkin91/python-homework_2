# #Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

print('Введите число : ')
n = int(input())
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
list = [factorial(i) for i in range(1, n + 1)] 

print(list)

