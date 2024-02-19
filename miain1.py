class functor:
    def __init__(self, func):
        self.func = func

    def __call__(self, num):
        if num < 0:
            raise ValueError("Number must be positive")
        else:
            return self.func(num)

@functor
def unchanged(num):
    return num

try:
    result = unchanged(1)
    print("Result: ", result)
except ValueError as v:
    print("Error: ", v)

try:
    result = unchanged(-1)
    print("Result: ", result)
except ValueError as v:
    print("Error: ", v)
