class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6


cube = Cube(4)
print(cube.surface_area())

