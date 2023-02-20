from graphic_object import GraphicObject


class Circle(GraphicObject):
    def __init__(self, color=None):
        super().__init__(color)
        
    @property
    def name(self):
        return 'Circle'
