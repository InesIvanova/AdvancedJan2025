import os

try:
    os.remove("my_first_file.txt")
    print("File deleted")
except FileNotFoundError:
    print("File already deleted!")