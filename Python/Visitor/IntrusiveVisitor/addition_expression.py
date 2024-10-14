from double_expression import DoubleExpression


class AdditionExpression:
    def __init__(self, left: DoubleExpression, right: DoubleExpression) -> None:
        self.left = left
        self.right = right

    def print(self, buffer: list) -> None:
        buffer.append("(")
        self.left.print(buffer)
        buffer.append("+")
        self.right.print(buffer)
        buffer.append(")")

    def eval(self) -> int:
        return self.left.eval() + self.right.eval()
