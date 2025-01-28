import os.path

file_path = os.path.join("files", "numbers.txt")
file = open(file_path)

content = file.read().split("\n")

total_sum = 0
for line in content:
    try:
        el = int(line)
        total_sum += el
    except ValueError:
        continue

print(total_sum)
print(file.read())
