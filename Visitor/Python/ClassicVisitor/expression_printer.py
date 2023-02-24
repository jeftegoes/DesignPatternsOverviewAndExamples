from addition_expression import AdditionExpression
from decorators import visitor
from double_expression import DoubleExpression


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @visitor(DoubleExpression)
    def visit(self, de):
        self.buffer.append(str(de.value))

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.buffer.append('(')
        ae.left.accept(self)
        self.buffer.append('+')
        ae.right.accept(self)
        self.buffer.append(')')

    def __str__(self):
        return ''.join(self.buffer)
