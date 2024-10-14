from renderer import Renderer


class VectorRenderer(Renderer):
    def renderer_circle(self, radius: int):
        print(f"Drawing a circle of radius {radius}")
