from modules_lecture.ex_4.core import execute

expression = input()

number1, sign, number2 = expression.split()
number1 = float(number1)
number2 = float(number2)

try:
    result = execute(number1, sign, number2)
except ZeroDivisionError:
    print("Can not divide by zero")
else:
    print(f"{result:.2f}")


