from double_expression import DoubleExpression


class AdditionExpression:
    def __init__(self, left: DoubleExpression, right: DoubleExpression):
        self.left = left
        self.right = right

    def accept(self, visitor):
        visitor.visit(self)
