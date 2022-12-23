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

# n = input()
# summ = 0
# for i in n:
#     if i.isdigit():
#         summ+=int(i)
# print(summ)

# n = float(input())
# len_num = len(str(n))-1
# summ=0
# while n!=int(n):
#     n= round(n*10,len_num)
#     print(n)
# while n>0:
#     summ+=n%10
#     n = n//10
# print(summ)
