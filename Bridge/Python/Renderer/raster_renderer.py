from renderer import Renderer


class RasterRenderer(Renderer):
    def renderer_circle(self, radius: int):
        print(f"Drawing pixels for circle of radius {radius}")
