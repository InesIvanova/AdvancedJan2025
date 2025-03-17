# def first_n(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
# elements = first_n(5)
# for el in elements:
#     print(el)
# sum_first_n = sum(first_n(5))
# print(sum_first_n)

def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield 'asd'

    n += 1
    print('This is printed at last')
    yield n


# print([el for el in range(1, 6)])
# print(my_gen())
result = my_gen()
for el in result:
    print(el)

# result = my_gen()
for el in result:
    print(el)
