from abc import abstractmethod, ABC, abstractproperty


class Person(ABC):
    def __init__(self, age):
        self.age = age

    @abstractmethod
    def greet(self):
        pass

    @property
    @abstractmethod
    def is_adult(self):
        return self.age >= 18


class Student(Person):
    def greet(self):
        return "Hi I a a student"

    @property
    def is_adult(self):
        return 'yes'

    def __call__(self, *args, **kwargs):
        print("object was called")

s = Student(20)
print(s())