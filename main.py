class Person:
    def __init__(self,):
        pass

    # def get_id(self):
    #     return self.__id


class Teacher(Person):
    def __init__(self, name, age, id, salary):
        super().__init__(name, age, id)
        self.salary = salary

    def __str__(self):
        return self._id


# p = Person("Test", 30, "000000")
# p.name = "asd"
# # print(p.name)
# # print(p.__id)
#



def define_name():
    return  "asd"

p = Person()
p2 = Person

if p is p2:
    print("a")
