
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
