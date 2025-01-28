with open("my_first_file.txt", "a") as file:
    file.write("I just created my first file!\n")
    print(file.closed)
print(file.closed)
