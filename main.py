def decorator(func):
    def wrapper(num):
        if num < 0:
            raise ValueError("Number must be positive")
        else:
            return func(num)

    return wrapper


@decorator
def unchanged(num):
    return num

try:
    result = unchanged(1)
    print("Result: ", result)
except ValueError as v:
    print("Error: ", v)

try:
    result = unchanged(-1)
    print("Result:", result)
except ValueError as v:
    print("Error:", v)
