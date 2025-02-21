n = int(input())


def print_row(spaces, stars):
    result = f"{' '*spaces}{'* '*stars}"
    print(result[:-1])


def print_upper_part(n):
    for row in range(1, n + 1):
        print_row(n - row, row)


def print_bottom_part(n):
    for row in range(1, n):
        print_row(row, n-row)

def print_rhombus(n):
    print_upper_part(n)
    print_bottom_part(n)


print_rhombus(n)
