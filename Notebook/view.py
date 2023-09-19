def get_op():
    op = int(input("1 - create_note, \n 2 - save_note, \n 3 - edit_note, \n 4 - delete_note, \n 5 - read_note, \n 6 - exit\n"))
    return op

def create_note():
    title = input("input title: ")
    message = input("input message: ")
    return title, message

def save_note():
    id = input("input id of a note to be saved: ")
    
    return id

def edit_note():
    id = input("input old note id: ")
    message = input("input new message: ")
    return  id, message


def delete_note():
    id = input("input id of a note to be deleted: ")
    return id

def read_note():
    id = input("input id of a note to be read: ")
    return id