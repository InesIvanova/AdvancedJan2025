from typing import Union
from dataclasses import dataclass


@dataclass()
class Animal:
    name: str
    age: int


a = Animal(name="Test", age=12)
b = Animal(name="Test", age=12)
print(a == b)
print(id(a))
print(id(b))

class Person:
    """
    Here is some example doc
    """
    kind = "mammal"

    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.__number = number

    def greet(self):
        """
        this is method which greets from user
        """
        return f"Hello, I am {self.name} and I am {self.age} years old."

    def celebrate_birthday(self):
        self.age += 1

    def change_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return "This is modified"

    def __repr__(self):
        return "from represent"

    def __add__(self, other):
        return self.age + other.age


p = Person("Test", 10, 10495768)
print(p._Person__number)
# # p2 = Person("Test2", 11)
# # p3 = Person("Test3", 12)
# #
# # Person.kind = "changed"
# # print(p.kind)
# # print(p2.kind)
# # print(p3.kind)
# #
# #
#
#
# class Person:
#     _id = 1
#
#     def __init__(self, name):
#         self.id = Person._id
#         self.name = name
#         Person._id += 1
#
#
# class Animal:
#     kind = "mammal"
#
#     def __init__(self, name):
#         self.name = name
#
# p = Person("test")
# p2 = Person("test2")
# p3 = Person("test3")
# print(p.id)
# print(p2.id)
# print(p3.id)
#
#
# class Person:
#     name = "George"
#     age = 25
#
# person = Person()
# p2 = Person()
# p3 = Person()
# print(person.name) # George
# print(person.age)  # 25
# print(p2.name) # George
# print(p2.age)  # 25
# print(p3.name) # George
# print(p3.age)  # 25
#
#
#
#


def sum_nums(a: Union[int, float], b: Union[int, float]) -> Union[float, int]:
    return a + b

print(sum_nums(5.6, 5.6))
