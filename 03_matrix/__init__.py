matrix = [[1, 2, 3], [4, 5, 6]]


for row in matrix:
    for el in row:
        print(el)


for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        print(matrix[row_index][col_index])