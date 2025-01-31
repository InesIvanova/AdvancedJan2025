chars_to_replace = ["-", ",", ".", "!", "?"]

with open("ex_files/ex_1.txt") as file:
    lines = file.readlines()

for index in range(0, len(lines), 2):
    for char_to_replace in chars_to_replace:
        lines[index] = lines[index].replace(char_to_replace, "@")
    current_words = reversed(lines[index].split())
    print(' '.join(current_words))
    # for w_index in range(len(current_line_words)-1, -1, -1):
    #     print(current_line_words[w_index], end=' ')

