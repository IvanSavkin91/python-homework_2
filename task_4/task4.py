# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

n = int(input('Введите число N '))
a = int(input('Введите число a '))
b = int(input('Введите число b '))
spam = list(range(-n, n+1))
print(spam)

mult = spam[a-1]*spam[b-1]
# mult = spam[a-1]*spam[b-1] если элемент имеется ввиду индекс
print(f'Произведение элементов на позиции(не индекс) {a} и {b} равно {mult}')