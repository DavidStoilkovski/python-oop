import functools


def even_parameters(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = None
        for el in args:
            if not type(el) == int or not el % 2 == 0:
                result = 'Please use only even numbers!'
                break

        if not result:
            result = func(*args)

        return result

    return wrapper

# Test code
# @even_parameters
# def add(a, b):
#     return a + b
#
# print(add(2, 4))
# print(add("Peter", 1))
#
# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))
