def cache(func):
    def wrapper(n):
        result = func(n)
        wrapper.log[n] = result
        return result

    wrapper.log = {}
    return wrapper

# Test code
# fibonacci(3)
# print(fibonacci.log)
#
# fibonacci(4)
# print(fibonacci.log)
