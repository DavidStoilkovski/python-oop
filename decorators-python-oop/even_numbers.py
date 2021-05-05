import functools


def even_numbers(function):
    @functools.wraps(function)
    def wrapper(numbers):
        return [num for num in numbers if num % 2 == 0]

    return wrapper

# Test code
# @even_numbers
# def get_numbers(numbers):
#     return numbers
# print(get_numbers([1, 2, 3, 4, 5]))
