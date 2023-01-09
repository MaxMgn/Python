import random
# len = randint(10, 15)
list = []
for i in range (random.randint(5, 20)):
    list.append(random.randint(1, 5))
print (list)
unique_el = [list [0]]
# unique_el.append(list [0]) 
for i in list:
    j = len(unique_el) 
    
    while True:
        if i == unique_el[j-1]:
            break
        j -= 1
        if j < 0:
            unique_el.append(i)
            break

print (unique_el)   