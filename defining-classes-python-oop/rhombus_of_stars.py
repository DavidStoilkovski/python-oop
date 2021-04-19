def draw_rhombus(i):
    return f"{' ' * (n - i)} {'* ' * i}".rstrip()


def create_rhombus(n):
    for upper in range(1, n + 1):
        print(draw_rhombus(upper))

    for lower in range(n - 1, -1, -1):
        print(draw_rhombus(lower))

    return None


n = int(input())

create_rhombus(n)

# Input
# 1
# 2
# 3
# 4
# 5 ...