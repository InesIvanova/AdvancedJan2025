def sum_nums(a, b):
    return a + b


def sub_nums(a, b):
    return a - b


mapper = {
    "+": sum_nums,
    "-": sub_nums,
    "*": lambda a, b: a*b,
    "/": lambda a, b: a/b,
    "^": lambda a, b: a**b,
}

def execute(num1, sign, num2):
    function = mapper[sign]
    return function(num1, num2)