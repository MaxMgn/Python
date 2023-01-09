import random
# path = '/Users/mustinov/Documents/Programming/Python/HW4/HW4_4.txt'
k = input("Enter k: ")
list = []
with open ('HW4_4.txt', 'w') as data:
    list.append(random.randint(0, 100))
    if list[0] != 0:
        data.write(str(list[0])+'*x**'+str(k))
    for i in range (1, k):
        list.append(random.randint(0, 100))
        if list[i] != 0:
            data.write(' + ' + str(list[i])+'*x**'+str(k-i))
    list.append(random.randint(0, 100))
    if list[k] != 0:
        data.write(' + ' + str(list[k]))
    data.write(" = 0")
data.close()
print (list)