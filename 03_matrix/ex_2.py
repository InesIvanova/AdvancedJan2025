# rows_count = int(input())
#
# matrix = []
#
# for _ in range(rows_count):
#     row_data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
#     matrix.append(row_data)
#
# print(matrix)
matrix[row_index][col_index]
print([[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(int(input()))])
