from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass




class Chair:
    def __init__(self, style):
        self.style = style


class Table:
    def __init__(self, style):
        self.style = style


class Sofa:
    def __init__(self, style):
        self.style = style


class ModernFactory(AbstractFactory):
    style = "modern"
    def create_chair(self):
        return Chair(self.style)

    def create_sofa(self):
        return Sofa(self.style)

    def create_table(self):
        return Table(self.style)


class FuturisticFactory(AbstractFactory):
    style = "futuristic"

    def create_chair(self):
        return Chair(self.style)

    def create_sofa(self):
        return Sofa(self.style)

    def create_table(self):
        return Table(self.style)