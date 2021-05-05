def vowel_filter(function):
    vowels = set('aeiouy' + 'aeiouy'.upper())

    def wrapper():
        data = function()
        return [ch for ch in data if ch in vowels]

    return wrapper

# Test code
# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
# print(get_letters())
