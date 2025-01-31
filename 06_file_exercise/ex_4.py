import os


dirs = input().split()
dir_path = ""
for dir_name in dirs:
    dir_path = os.path.join(dir_path, dir_name)


data = {}


def traverse(dir_path, level=0):
    if level > 1:
        return
    try:
        for file in os.listdir(dir_path):
            path = os.path.join(dir_path, file)
            if os.path.isfile(path):
                file_name, extension = file.split(".")
                if extension not in data:
                    data[extension] = []
                data[extension].append(file)
            else:
                nested_path = os.path.join(dir_path, file)
                traverse(nested_path, level+1)

    except FileNotFoundError:
        print("Invalid dir name or path to dir")

traverse(dir_path)

result = ""
for extension, files in sorted(data.items(), key=lambda kvp: kvp[0]):
    result += f".{extension}\n"
    for file_name in sorted(files):
        result += f"- - - {file_name}\n"

report_path = os.path.join(dir_path, "report.txt")
with open(report_path, "w") as file:
    file.write(result)

