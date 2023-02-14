def get_op():
    op = int(input("1 - input student, \n 2 - input subject,\n 3 - input mark,\n 4 - display list,\n 5 - display the student, \n 6 - exit\n"))
    return op

def input_student():
    name = input("input student")
    return name

def input_subject():
    subject = input("input subject")
    return subject

def get_mark():
    name = input("input student ")
    subject = input("input subject ")
    mark = input("input mark")
    return name,subject,mark

def input_student_table():
    name = input("input student")
    return name