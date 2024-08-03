from functools import reduce
from math import floor


def add(*args):
    return sum(args)


def square(a):
    return a * a


def splitter(a):
    floored = floor(a / 2)
    return [floored, a - floored]


def my_max(a):
    return max(a) if isinstance(a, list) else a


def my_min(a):
    return min(a) if isinstance(a, list) else a


def compose(*functions):
    def composed_function(*args, **kwargs):
        return reduce(
            lambda acc, fn: fn(acc), functions[1:], functions[0](*args, **kwargs)
        )

    return composed_function


# Example usage:
composed = compose(add, splitter, my_max)
result = composed(
    2, 1, 3
)  # This will pass 2, 1, 3 to the add function and then pass its output through the rest of the functions.
print(result)  # Expecting the result of the composed function calls.
