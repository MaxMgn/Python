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


# import random
#
# n = int(input())
# list_num = [random.randint(-n,n) for i in range(n)]
# print(list_num)

# file = open("File.txt","r")
# multi = 1
# list_str = file.readlines()
# print(list_str)
# list_num = list(map(str.strip,list_str))
# print(list_num)
# list_num = list(map(int,list_num))
# print(list_num)
# for i in file:
#     multi*=list_num[int(i)]
# print(multi)

