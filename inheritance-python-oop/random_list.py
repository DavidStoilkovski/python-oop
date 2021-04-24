import random


class RandomList(list):

    def get_random_element(self):
        random_index = random.randint(0, len(self) - 1)
        element = self.pop(random_index)
        return element
