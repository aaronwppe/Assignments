import switch


class Quadrilateral:
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4


class Rectangle(Quadrilateral):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

        super().__init__(length, breadth, length, breadth)

    @property
    def area(self):
        return self.length * self.breadth


class Square(Quadrilateral):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side, side, side)

    @property
    def area(self):
        return self.side ** 2


while 1:
    try:
        print('Rectangle:')
        length = int(input('Length = '))
        breadth = int(input('Breadth = '))

        rectangle = Rectangle(length, breadth)
        print(f'Perimeter = {rectangle.perimeter}')
        print(f'Area = {rectangle.area}')
        break

    except ValueError:
        print("ERROR: Values provided must be of type 'int'!")

print()

while 1:
    try:
        print('Square:')
        side = int(input('Side = '))

        square = Square(side)
        print(f'Perimeter = {square.perimeter}')
        print(f'Area = {square.area}')
        break

    except ValueError:
        print("ERROR: Values provided must be of type 'int'!")

