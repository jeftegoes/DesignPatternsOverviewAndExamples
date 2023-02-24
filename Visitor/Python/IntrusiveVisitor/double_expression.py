class DoubleExpression:
    def __init__(self, value: int) -> None:
        self.value = value

    def print(self, buffer: list) -> None:
        buffer.append(str(self.value))

    def eval(self) -> int:
        return self.value
