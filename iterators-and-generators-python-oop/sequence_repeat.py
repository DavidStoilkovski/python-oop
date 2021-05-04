class sequence_repeat:

    def __init__(self, string, repeat):
        self.string = string
        self.repeat = repeat
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.repeat == 0:
            raise StopIteration

        if self.index == len(self.string):
            self.index = 0

        index = self.index
        self.index += 1
        self.repeat -= 1
        return self.string[index]

# Test code
# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')
