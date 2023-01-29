# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
a = [float(input(f'Введите {e} координату точки а ')) for e in 'xy']
b = [float(input(f'Введите {e} координату точки b ')) for e in 'xy']

distance = sum([(i[1] - i [0]) ** 2 for i in  zip (a, b)])** 0.5
print("distance = ", distance)