class Point:
    import math

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x_cord, y_cord):
        x_distance = abs(x_cord - self.x)
        y_distance = abs(y_cord - self.y)
        distance = Point.math.sqrt(x_distance ** 2 + y_distance ** 2)
        return distance

# Test code
# p = Point(2, 4)
# p.set_x(3)
# p.set_y(5)
# print(p.distance(10, 2))
