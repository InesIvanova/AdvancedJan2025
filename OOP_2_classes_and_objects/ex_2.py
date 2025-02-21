class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x: int) -> None:
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def __repr__(self):
        return "from repr"

    def __str__(self) -> str:
        return f"The point has coordinates ({self.x},{self.y})"

    def status(self) -> str:
        return "from status"


p = Point(2, 4)
print(p)

a = 5
print(p.status())