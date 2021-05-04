class custom_range:
    def __init__(self, start, end):
        self.index = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        current_index = self.index
        if current_index > self.end:
            raise StopIteration
        self.index += 1
        return current_index

# Test code
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)
