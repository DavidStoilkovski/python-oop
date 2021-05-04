class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(dictionary)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.index < len(self.dictionary):
            raise StopIteration

        key = self.keys[self.index]
        value = self.dictionary[key]

        self.index += 1

        return key, value

# Test_code
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
