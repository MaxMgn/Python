#

def polynom_file_to_list(file):
    with open (file, 'r') as data :
        for line in data:
            polynom = line.replace(" = 0", "")
            polynom = polynom.split("+")
            polynom[0].replace(" ", "")
            degree_prev = int(polynom[0].split("^")[1])
            coeff_list = [int(polynom[0].split("*")[0])]
            if len(coeff_list) != 1:
                for i in range (1, len(polynom)):
                    polynom[i].replace(" ", "")
                    if "^" not in polynom[i]:
                        degree = 0
                    else:
                        degree = int(polynom[i].split("^")[1])
                    while degree_prev - degree != 1:
                        coeff_list.append(0)
                        degree_prev -= 1
                    degree_prev = degree
                    coeff_list.append(int(polynom[i].split("*")[0]))
            else:
                while degree_prev !=0:
                    coeff_list.append(0)
                    degree_prev -=1
            coeff_list.reverse()
            return coeff_list   
    data.close()        

coeff_listA = polynom_file_to_list("HW4_5_a.txt")
coeff_listB = polynom_file_to_list("HW4_5_b.txt")
while len(coeff_listA) != len(coeff_listB):
    if len(coeff_listA) > len(coeff_listB):
        coeff_listB.append(0)
    else:
        coeff_listA.append(0)
coeff_list_sum = []
for i in range (len(coeff_listA)):
    coeff_list_sum.append(coeff_listA[i] + coeff_listB[i])
coeff_list_sum.reverse()

print(coeff_listA)
print(coeff_listB)
print(coeff_list_sum)

with open ('HW4_5_sum.txt', 'w') as sum:
    sum.write(str(coeff_list_sum[0]) +'*x^'+str(len(coeff_list_sum)-1))
    for i in range (1, len(coeff_list_sum)-1):
        if coeff_list_sum[i] != 0:
            sum.write(' + ' + str(coeff_list_sum[i])+'*x^'+str(len(coeff_list_sum)-i-1))
    if coeff_list_sum[len(coeff_list_sum) - 1] != 0:
        sum.write(str(coeff_list_sum[len(coeff_list_sum) - 1]))
    sum.write(" = 0")
sum.close()