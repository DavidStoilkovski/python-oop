import functools


def multiply(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(params):
            return times * func(params)

        return wrapper

    return decorator

# Test code
# @multiply(3)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(3))
#
# @multiply(5)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(6))
