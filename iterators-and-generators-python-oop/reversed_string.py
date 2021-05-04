def reverse_text(string):
    for i in range(len(string) - 1, -1, -1):
        yield string[i]

# Test code
# for char in reverse_text("step"):
#     print(char, end='')
