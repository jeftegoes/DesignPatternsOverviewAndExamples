from buffer import Buffer
from view_port import Viewport


class Console:
    def __init__(self) -> None:
        buffer = Buffer()
        self.current_viewport = Viewport(buffer)
        self.buffers = [buffer]
        self.viewports = [self.current_viewport]

    def write(self, text):
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)
