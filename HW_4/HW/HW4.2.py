num = input("insert number: ")
def primelist (num):
    primelist = [2]
    for i in range(3, num+1):
        is_prime = True
        for j in range(len(primelist)):
            if (i % primelist[j-1] == 0):
                is_prime = False
        if is_prime:
            primelist.append(i)
    return primelist
primelist = (primelist(num)) 

prime_multiplier_list = []
e = 0
while (num > 1 or e < len(primelist)):
    # for e in range(len(primelist)):
        while (num % primelist[e] == 0):
            num /= primelist[e]
            prime_multiplier_list.append(primelist[e])
        e+=1
print (prime_multiplier_list)