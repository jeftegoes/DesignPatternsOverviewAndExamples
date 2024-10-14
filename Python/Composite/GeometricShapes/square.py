from graphic_object import GraphicObject


class Square(GraphicObject):
    def __init__(self, color=None):
        super().__init__(color)

    @property
    def name(self):
        return 'Square'
