n = int(input())

sum_diagonal = 0

for current_index in range(n):
    row_data = [int(el) for el in input().split()]
    sum_diagonal += row_data[current_index]

print(sum_diagonal)