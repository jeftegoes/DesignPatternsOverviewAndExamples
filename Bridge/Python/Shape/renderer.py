from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None
