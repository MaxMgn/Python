import datetime
import view

notebook = {}
note = []
subjects_list = []
id_count = 0
file_is_not_empty = False
def start():
    file_is_not_empty = False
    while True:
        print("")
        print("NOTEBOOK")
        print("")
        for i in notebook:
            print(i + ": ")
            print(notebook[i])
        print("")
        op = view.get_op()
        if op == 1:
            id_count = len(notebook)
            title, msg = view.create_note()
            notebook[str(id_count)] = []
            notebook[str(id_count)].append(title)
            notebook[str(id_count)].append(msg)
            notebook[str(id_count)].append(datetime.datetime.now().strftime("%Y-%B-%D %H:%M:%S"))
        if op == 2:
            id = view.save_note()
            with open ('notebook.txt', 'a') as data:
                if file_is_not_empty:
                    data.write(",")
                data.write( id + ";" + notebook[id][0] + ";" + notebook[id][1] + ";" + notebook[id][2] )
                data.close()
                file_is_not_empty = True
        if op == 3:
            id, msg = view.edit_note()
            notebook[id][1] = msg
        if op == 4:
            id = view.delete_note()
            notebook[id] = None
        if op == 5:
            id = view.read_note()
            print(notebook[id])
        if op == 6:
            break