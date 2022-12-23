# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
n = int(input('Введите число: '))
dic = {}
for i in range(1, n+1):
    dic[i] = round((1+1/i)**i,2)
print(dic)
print(sum(dic.values()))



