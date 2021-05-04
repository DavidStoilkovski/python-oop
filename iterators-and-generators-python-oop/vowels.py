class vowels:
    all_vowels = (
        'A', 'E', 'I', 'O', 'U', 'Y',
        'a', 'e', 'i', 'o', 'u', 'y',
    )

    def __init__(self, string):
        self.string = string
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.string):
            raise StopIteration

        ch = self.string[self.current_index]
        self.current_index += 1

        if ch in vowels.all_vowels:
            return ch

        return self.__next__()

# Test code
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
