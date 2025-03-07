class Person:
    def __init__(self, id):
        self.id = id
        self.age = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if self.id.startswith("94"):
            self.__age = 30

    @staticmethod
    def is_adult(age):
        return age >= 18


p = Person("9408191212")
print(p.age)
print(p.is_adult(19))