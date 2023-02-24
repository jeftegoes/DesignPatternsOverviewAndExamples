from double_expression import DoubleExpression
from expression import Expression


class AdditionExpression(Expression):
    def __init__(self, left: DoubleExpression, right: DoubleExpression) -> None:
        self.left = left
        self.right = right
