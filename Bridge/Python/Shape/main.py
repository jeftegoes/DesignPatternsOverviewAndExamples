from raster_renderer import RasterRenderer
from square import Square
from triangle import Triangle
from vector_renderer import VectorRenderer

sq = Square(VectorRenderer())
print(sq)

tr = Triangle(RasterRenderer())
print(tr)
