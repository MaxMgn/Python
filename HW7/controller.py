import  model
import view


def start():
    while True:
        command = view.command()
        if command == 1:
            view.add_record()
        elif command == 2:
            model.print_data()
        elif command == 3:
            view.print_name_surname()
        elif command  == 4:
            break
