from abc import ABC

from renderer import Renderer


class Shape(ABC):
    def __init__(self, renderer: Renderer, name) -> None:
        self.renderer: Renderer = renderer
        self.name: str = name

    def __str__(self) -> str:
        return 'Drawing %s as %s' % (self.name, self.renderer.what_to_render_as)