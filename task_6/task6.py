# Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

s, n = input(), input()
length_n = len(n)
total = 0
for i in range(len(s)):
    if s[i:i + length_n] == n:
        total += 1
        print(total)