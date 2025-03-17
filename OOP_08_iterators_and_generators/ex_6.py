def  reverse_text(text):
    index = len(text) - 1
    while index >= 0:
        yield text[index]
        index -= 1

for char in reverse_text("step"):
    print(char, end='')
