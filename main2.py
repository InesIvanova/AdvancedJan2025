def small_letters(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()
    return wrapper


def cap_letters(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@small_letters
@cap_letters
def letters():
    return "AakAkka"



class A:
    @staticmethod
    def hi():
        return "hi"


a = A()
print(a.hi())
print(A.hi())