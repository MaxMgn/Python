# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
n = int(input('Введите число: '))
sum = 0
for i in range(1, n+1):
    sum = (1 + 1/i) ** i + sum
print(round(sum, 2))