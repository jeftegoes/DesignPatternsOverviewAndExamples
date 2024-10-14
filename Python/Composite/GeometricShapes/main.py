from circle import Circle
from graphic_object import GraphicObject
from square import Square

drawing = GraphicObject()
drawing._name = 'My Drawing'
drawing.children.append(Square('Red'))
drawing.children.append(Circle('Yellow'))

group = GraphicObject()
group.children.append(Circle('Blue'))
group.children.append(Square('Blue'))
drawing.children.append(group)

print(drawing)
