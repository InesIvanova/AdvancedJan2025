def genrange(start, end):
    temp = start
    while temp <= end:
        yield  temp
        temp += 1

result = genrange(1, 10)
for el in result:
    print(el)
