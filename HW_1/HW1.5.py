# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))
distance = round(((x2 - x1) ** 2 + (y2 - y1 ) ** 2) ** (1/2), 2)
print("distance = ", distance)