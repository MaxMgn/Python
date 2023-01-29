# 46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)
import random
l = [random.randint(1,10) for i in range(6)]
multiplication_list = [l[indx]*l[-indx-1] for indx in range(len(l)//2+len(l)%2)]
print(l)
print(multiplication_list)