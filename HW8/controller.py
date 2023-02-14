import view

dictionary = {}
names_list = []
subjects_list = []

def start():
    while True:
        print(dictionary)
        op = view.get_op()
        if op == 1:
            name = view.input_student()
            if name not in names_list:
                names_list.append(name)
                dictionary[name] = {}
                for subject in subjects_list:
                    dictionary[name][subject] = []
        if op == 2:
            subject = view.input_subject()
            if subject not in subjects_list:
                subjects_list.append(subject)
                for name in names_list:
                    dictionary[name][subject] = []
        if op == 3:
            name, subject, mark = view.get_mark()
            dictionary[name][subject].append(mark)
        if op == 4:
            print(dictionary)
        if op == 5:
            name = view.input_student_table()
            print(dictionary[name])
        if op == 6:
            break