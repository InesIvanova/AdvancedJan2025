

for i in range(1, 5):
    for j in range(1, 3):
        print(i)

def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    def area():
        return width * length

    def perimeter():
        return 2*width + 2*length

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))