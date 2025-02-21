class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed =max_speed
        self.gadgets = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)




class Animal:
    color = "red"
    def __init__(self, name):
        self.name = name
        self.tricks = []



Animal.kind = "something else"
cat = Animal("Lady")
dog = Animal("Sharo")
dog2 = Animal("Ares")
dog.tricks.append("jump")
print(cat.tricks)
print(dog.tricks)
print(dog2.tricks)
cat.tricks.append("sit")



