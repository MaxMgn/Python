# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
quarter = input('Введите номер четверти: ')
if quarter.isdigit():
    quarter = int(quarter)
else:
     print ('Введено нечисловое значение')
     exit()
if (quarter == 1): 
    print ('x > 0 and y > 0')
elif (quarter == 2): 
    print ('x < 0 and y > 0')
elif (quarter == 3): 
    print ('x < 0 and y < 0')
elif (quarter == 4): 
    print ('x > 0 and y < 0')
else: 
    print ('Введено некоректное значение')