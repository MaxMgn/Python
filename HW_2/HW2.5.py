# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
list1 = [1, 2, 3, 2, 0]
list2= [5, 1, 2, 7, 3, 2]
result = []

templist = list2
for i in list1:
    if i in templist:
        result.append(i)
        templist.remove(i)

print (result)
