# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from encodings import utf_8
from random import *
list = []
n = int(input("Введите n: "))
for _ in range (n):
    list.append(randint(-n, n+1))
print (list)
with open ('file.txt', 'w', encoding = 'utf-8') as f:
    for _ in range (randint(2, 5)):
        f.write(str(randint(0, n-1)) + '\n')
mult = 1
with open ('file.txt', 'r', encoding = 'utf-8') as f:
    f = f.read().splitlines()
    for el in f:
        mult *= list [int(el)]
print (mult)


