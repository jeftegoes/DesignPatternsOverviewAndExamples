from math import pi


class Square:
    def __init__(self, side: int = 0):
        self.side = side

    def calculate_area(self) -> int:
        return self.side ** 2


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> int:
        return self.width * self.height


class SquareToRectangleAdapter:
    def __init__(self, square: Square) -> None:
        self.square = square

    @property
    def width(self) -> int:
        return self.square.side

    @property
    def height(self):
        return self.square.side

    def calculate_area(self) -> int:
        return self.width * self.height


class SquareToCircleAdapter:
    def __init__(self, square: Square) -> None:
        self.square = square

    def radius(self) -> float:
        return self.square.side

    def calculate_area(self) -> int:
        return (pi * self.radius() ** 2)


square = Square(2)
print(f"1: Area of Square is: {square.calculate_area()}")


rectangle = Rectangle(2, 4)
print(f"2: Area of Rectangle is: {rectangle.calculate_area()}")

square = Square(11)
squareToRectangleAdapter = SquareToRectangleAdapter(square)
print(
    f"3: Area of Rectangle with Adapter is: {squareToRectangleAdapter.calculate_area()}")

squareToCircleAdapter = SquareToCircleAdapter(Square(1.1))
squareToCircleAdapter.calculate_area()
print(
    f"4: Area of circle with Adapter is: {squareToCircleAdapter.calculate_area()}")
