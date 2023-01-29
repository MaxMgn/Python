# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позициях.
lst = [2, 3, 5, 9, 3]
filteredlst = list(filter(lambda x: x[0]%2, enumerate(lst)))
zippedlst = list(zip (filteredlst[0], filteredlst[1]))
sum_lst = sum(zippedlst[1])
# print(sum)
# for i in range (1, len(list)):
#     sum += list[i]
print("сумма элементов списка, стоящих на нечётной позициях: ", sum_lst)