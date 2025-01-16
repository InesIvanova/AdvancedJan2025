rows_count = int(input())

result = []
for _ in range(rows_count):
    for el in input().split(", "):
        result.append(int(el))

print(result)