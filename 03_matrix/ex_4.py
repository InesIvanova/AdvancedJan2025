data = input().split(", ")
row_count = int(data[0])
col_count = int(data[1])

matrix = []

for _ in range(row_count):
    data_row = [int(el) for el in input().split()]
    matrix.append(data_row)

for col_index in range(col_count):
    col_sum = 0
    for row_index in range(row_count):
        col_sum += matrix[row_index][col_index]
    print(col_sum)
