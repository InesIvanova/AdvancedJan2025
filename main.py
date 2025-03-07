from abc import ABC, abstractmethod



class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        return None

class Square(Shape):
    side_length = 2
    def calculate_area(self):
        return self.side_length * 2

class Triangle(Shape):
    base_length = 4
    height = 3
    def calculate_area(self):
        return 0.5 * self.base_length * self.height

class Rectangle(Shape):
    def calculate_area(self):
        return "returrning area of rect"


s = Shape()
print(s)
