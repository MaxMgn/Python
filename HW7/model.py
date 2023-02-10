def print_data():
    with open("telbook.txt","r") as file:
        for line in file.readlines():
            print(line)

def print_name_surname():
    with open("telbook.txt","r") as file:
        for line in file.readlines():
            temp = line.split(",")
            print("Name: " - temp[1], " Surname " - temp[2])