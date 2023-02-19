from renderer import Renderer


class Shape:
    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass
