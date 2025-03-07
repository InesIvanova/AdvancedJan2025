from pandas.errors import PerformanceWarning


def is_adult(age):
    return age >= 18


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_underaged_person(cls, name):
        return cls(name, 17)


p = Person("test", 12)
p2 = Person.create_underaged_person("test2")
print(p2.age)



class Pizza:
    def __init__(self, *ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls("domato", "peperonni", "yellow cheeze")

    @classmethod
    def margarita(cls):
        return cls("domato", "yellow cheeze")



p1 = Pizza("cheeze", "mozarella", "third cheese", "fourth cheese")

p2 = Pizza("domato", "peperonni", "yellow cheeze")
p3 = Pizza("domato", "peperonni", "yellow cheeze")

p4 = Pizza("domato", "peperonni", "yellow cheeze")

p5 = Pizza("domato", "peperonni", "yellow cheeze")

p6 = Pizza.pepperoni()

p7 = Pizza.margarita()


prefered_piza = input()
if prefered_piza.lower() == "margarita":
    Pizza("....")


