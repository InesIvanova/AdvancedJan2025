from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [el for el in result if el.lower() in 'aeuyoi']
    return wrapper



@vowel_filter
def get_letters(letters):
    return letters


@vowel_filter
def get_special_letter(a, b):
    letters = (a, b)
    return letters


@vowel_filter
def third_special_letter():
    return ['t', 'o']

print(get_letters(['a', 'b', 'e', 'c']))
print(get_special_letter("u", "r"))
print(third_special_letter())
