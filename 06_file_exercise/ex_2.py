from string import punctuation


with open("ex_files/ex_1.txt") as file:
    lines = file.readlines()


result = ""
for index in range(len(lines)):
    n_chars = 0
    n_punc = 0
    for char in lines[index]:
        if char in punctuation:
            n_punc += 1
        if char.isalpha():
            n_chars += 1
    # lines[index] = lines[index].replace("\n", "")
    lines[index]= lines[index].rstrip("\n")
    result += f"Line {index+1}: {lines[index]} ({n_chars})({n_punc})\n"

with open("ex_files/ex_2_output.txt", "w") as file:
    file.write(result)