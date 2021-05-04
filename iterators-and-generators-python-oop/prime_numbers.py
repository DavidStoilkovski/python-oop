from math import sqrt


def get_primes(nums):
    for num in nums:
        if num > 1:
            is_prime = True
        else:
            is_prime = False

        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False

        if is_prime:
            yield num

# Test code
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
