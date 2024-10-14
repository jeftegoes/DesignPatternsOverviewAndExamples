from buffer import Buffer


class Viewport:
    def __init__(self, buffer: Buffer) -> None:
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index+self.offset]

    def append(self, text):
        self.buffer += text