class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        name = self.name + " " + other.name
        age = self.age + other.age
        return Person(name, age)


    # def concat_people(self, other):
    #     name = self.name + " " + other.name
    #     age = self.age + other.age
    #     return Person(name, age)


p1 = Person("Test", "40")
p2 = Person("Tes2", 41)

p3 = p1 + p2

print(p3.name)
print(p3.age)