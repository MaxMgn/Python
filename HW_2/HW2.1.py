# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
str = input('Введите число: ')
number_of_digit = len(str)
index_point = str.find('.') 
sum = 0
n = float(str)

 
if float(n) % 1 != 0:
    n = n * 10 ** (number_of_digit- index_point - 1)
    number_of_digit -= 1
for i in range(number_of_digit):
        sum += n % 10
        n //= 10
print('сумма цифр = ' , sum)