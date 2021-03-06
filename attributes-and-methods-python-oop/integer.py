class Integer:
    import math

    def __init__(self, value):
        self.value = value

    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

    @classmethod
    def from_float(cls, value):
        if not type(value) == float:
            return f"value is not a float"

        value = cls.math.floor(value)
        return cls(value)

    @classmethod
    def from_roman(cls, value):
        value = cls.roman_to_int(cls, value)
        return cls(value)

    @classmethod
    def from_string(cls, value):

        if not type(value) == str:
            return "wrong type"

        return cls(int(value))

    def add(self, integer):
        if not type(integer) == Integer:
            return "number should be an Integer instance"

        return self.value + integer.value

# Test code
# first_num = Integer(10)
# second_num = Integer.from_roman("IV")
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
# print(first_num.add(second_num))
