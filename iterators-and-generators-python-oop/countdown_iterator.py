class countdown_iterator:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        current = self.start

        if current < 0:
            raise StopIteration

        self.start -= 1
        return current

# Test code
# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")
