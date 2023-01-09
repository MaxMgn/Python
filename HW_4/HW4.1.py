d = input("insert 0.0000000001 < d < 0.1:  ")
num = input("insert number: ")
def place (d):
    place = 0
    while (d < 1):
        d *= 10
        place += 1
    return place
print(round(num, place(d)))