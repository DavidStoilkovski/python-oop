class reverse_iter:
    def __init__(self, list_of_numbers):
        self.list_of_numbers = list_of_numbers
        self.last_element_index = len(list_of_numbers) - 1

    def __iter__(self):
        return self

    # def __reversed__(self):
    #     return self

    def __next__(self):
        current = self.last_element_index
        if current < 0:
            raise StopIteration
        self.last_element_index -= 1
        return self.list_of_numbers[current]

# Test code
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)
