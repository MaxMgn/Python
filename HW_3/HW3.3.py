# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list = [1.1, 1.2, 3.1, 5, 10.01]
max = 0
min = 1
for i in range(len(list)):
    print (list[i])
    if list[i] % 1 != 0:
        fractional_part = float("0."+str(list[i]).split('.')[1])
        if max < fractional_part:
            max = fractional_part
        if min > fractional_part:
            min = fractional_part
print (max - min)