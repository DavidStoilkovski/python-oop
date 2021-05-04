class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        current = self.index

        if self.count <= 0:
            raise StopIteration

        self.index += self.step
        self.count -= 1

        return current

# Test code
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
#
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)
