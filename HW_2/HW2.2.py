# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите число: '))
mult = 1
print('[', end='')
for i in range(1, n):
    mult *= i 
    print(mult, end=', ')
print(mult*n, end=']')