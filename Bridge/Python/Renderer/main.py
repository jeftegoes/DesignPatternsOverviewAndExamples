from circle import Circle
from raster_renderer import RasterRenderer
from vector_renderer import VectorRenderer

raster = RasterRenderer()
vector = VectorRenderer()
circle = Circle(vector, 5)
circle.draw()
circle.resize(2)
circle.draw()
