from itertools import permutations


def possible_permutations(nums):
    for el in permutations(nums):
        yield list(el)

# Test code
# [print(n) for n in possible_permutations([1, 2, 3])]
