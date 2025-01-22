def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power-1)



a = {"a": {1: [{'f': 1}]}, "b": [1, 2, 3], "c": {0: {1: {2: {"c": [{"k": 3}]}}}}}


def obtain_softuni_courses(n=3):
    res = requsts.get("https://softuni.bg/trainings/4839/python-advanced-january-2025")
    if res.status in (500, 503):
        if n != 0:
            obtain_softuni_courses()

        else:
            return "Softuni is not available"
    else:
        return res.data

print(recursive_power(2, 4))
print(recursive_power(10, 100))


