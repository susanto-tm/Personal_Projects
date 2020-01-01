class Shape:
    def __init__(self, color='black', filled=False):
        self.color = color
        self.filled = filled

    def get_color(self):
        return self.color

    def get_filled(self):
        return self.filled


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4*self.length


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return int((22/7) * self.radius * self.radius)

    def perimeter(self):
        return int((22/7) * 2 * self.radius)


square = Square(4)
circle = Circle(2)

print(square.area(), circle.area())
print(square.get_color(), circle.get_color())
print(square.get_filled(), circle.get_filled())
