from shape import Shape


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Square')
