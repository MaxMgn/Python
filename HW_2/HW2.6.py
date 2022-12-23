
import time
from random import *
n = int(input("Введите n: "))
list = []
for _ in range (n):
        list.append(randint(-n, n+1))
print ("list before shuffling ", list)
for _ in range (randint(1, 5)):
    i1 = randint(0, n-1)
    i2 = randint(0, n-1)
    list[i1], list [i2] = list[i2], list [i1]
print ("list after shuffling ", list)

# import datetime
# def random_int(num):
#     rand = datetime.datetime.now().microsecond/10**6
#     return int(num*rand)

# a = [1,2,3,4,5,6]
# print(a)
# random_int(5)
# for i in range(len(a)-1,-1,-1):
#     j = random_int(i+1)
#     a[i],a[j] = a[j],a[i]
# print(a)
