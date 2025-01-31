import os

command = input()

while command != "End":
    data = command.split("-")
    file_name = data[1]
    if command.startswith("Create"):
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            with open(file_name, 'w') as fp:
                pass
    elif command.startswith("Add"):
        content = data[2] + "\n"
        with open(file_name, "a") as file:
            file.write(content)
    elif command.startswith("Replace"):
        old_string = data[2]
        new_string = data[3]
        try:
            with open(file_name, "r+") as file:
                content = file.read()
                file.seek(0)
                file.truncate()
                file.write(content)
        except FileNotFoundError:
            print("An error occurred")
    elif command.startswith("Delete"):
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
    command = input()