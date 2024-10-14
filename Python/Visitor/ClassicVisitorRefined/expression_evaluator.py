from addition_expression import AdditionExpression
from decorators import visitor
from double_expression import DoubleExpression


class ExpressionEvaluator:
    def __init__(self):
        self.value = None

    @visitor(DoubleExpression)
    def visit(self, de):
        self.value = de.value

    @visitor(AdditionExpression)
    def visit(self, ae):
        # ae.left.accept(self)
        self.visit(ae.left)
        temp = self.value
        # ae.right.accept(self)
        self.visit(ae.right)
        self.value += temp
