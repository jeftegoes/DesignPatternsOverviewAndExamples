class Buffer:
    def __init__(self, width=30, height=20) -> None:
        self.width = width
        self.height = height
        self.buffer = [" "] * (width*height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text
