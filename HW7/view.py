def command(): 
    command = int(input(" 1 - add_record \n 2 - print table \n 3 - print only name & surname \n 4 - exit\n"))
    return command

def add_record():
    id = input("id ")
    name = input()
    lastname  = input()
    number = input()
    comments = input()
    line = id + ", " + name + ", " + lastname + ", " + number + ", "+ comments
    with open("telbook.txt","a") as file:
        file.write(line)
        file.close
    print("saved")
    