data = input().split(", ")
row_count = int(data[0])
col_count = int(data[1])

matrix = []
sum_elements = 0


for row_index in range(row_count):
    data_row = [int(el) for el in input().split(", ")]
    # sum_elements += sum(data_row)
    matrix.append(data_row)


#
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         sum_elements += matrix[row_index][col_index]

print(sum(map(sum, matrix)))

print(matrix)