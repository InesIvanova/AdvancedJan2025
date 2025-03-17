# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.current_index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current_index += 1
#
#         if self.current_index >= len(self.name):
#             raise StopIteration
#         return self.name[self.current_index]
#         # self.current_index += 1
#         # self.age_index += 1
#         # if self.current_index >= len(self.name):
#         #     raise StopIteration
#         # if self.age_index >= len(self.age_as_str):
#         #     self.age_index = 0
#         # return f"{self.name[self.current_index]} {self.age_as_str[self.age_index]}"
#
#     def __add__(self, other):
#         return self.age + other.age
#
#
#     def generate(self, end):
#         num = 0
#         while num <= end:
#             yield num
#             num +=1
#
#
#
# p = Person("Testasdascfas", 12)
# result = p.generate(6)
# for el in result:
#     print(el)
# for i in p:
#     print(i)
#
#
# a = "100.5"
# print(type(a))
# for i in a:
#     print(i)
#
# # iter_p = iter(p)
# # while True:
# #     try:
# #         print(next(iter_p))
# #     except StopIteration:
# #         break
#
# # my_list = [4, 7, 0, 3]
# #
# # for num in my_list:
# #     print(num)
# #
# #
# # my_iter = iter(my_list)
# # while True:
# #     try:
# #         print(next(my_iter))
# #     except StopIteration:
# #         break
# #
# # my_iter = iter(my_list)
# #
# # while True:
# #     try:
# #         print(next(my_iter))
# #     except StopIteration:
# #         break

print(reversed([1,2 ,3]))