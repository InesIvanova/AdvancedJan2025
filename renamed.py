class A:
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def a(self):
        return "a"



class B(A):
    # def __init__(self, name, age, salary):
    #     super().__init__(name, age)
    #     self.salary = salary

    def a(self):
        return "asd"

    def b(self):
        res = self.a()
        return f"{res} a from B class"



b = B()
print(b.a())
print(b.c())