from renderer import Renderer
from shape import Shape


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: int) -> None:
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.renderer_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor
