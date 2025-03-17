def squares(n):
    current = 1

    while current <= n:
        yield  current ** 2
        current += 1

nums = []
result = squares(5)
for el in result:
    nums.append(el)
    print(el)   
# print(list(squares(5)))
print(nums)