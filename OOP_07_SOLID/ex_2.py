from abc import ABC, abstractmethod


class Animal(ABC):
    pass

class SilentAnimal(Animal):
    @abstractmethod
    def be_scary(self):
        pass


class SoundAnimal(Animal):
    @abstractmethod
    def make_sound(self):
        pass



class Dog(SoundAnimal):
    def make_sound(self):
        return "woof-woof"

    def sniff_for_people(self):
        return "sniffing for missing personc"

class Cat(SoundAnimal):
    def make_sound(self):
        return "meow"


class Pig(SoundAnimal):
    def make_sound(self):
        return "oink"


class Snake(SilentAnimal):
    def be_scary(self):
        return "looks green"


def animal_sound(animals: list[SoundAnimal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Pig()]
animal_sound(animals)


print(SoundAnimal.mro())
