def multiply(*args):
    if not args:
        return "Can not multiply - no args"

    result = 1
    for el in args:
        result *= el
    return result
