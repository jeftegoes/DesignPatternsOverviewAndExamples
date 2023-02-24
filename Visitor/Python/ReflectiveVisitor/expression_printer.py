from addition_expression import AdditionExpression
from double_expression import DoubleExpression
from expression import Expression


class ExpressionPrinter:
    @staticmethod
    def print(e, buffer):
        """ Will fail silently on a missing case. """
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(e.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(')')

    Expression.print = lambda self, b: ExpressionPrinter.print(self, b)
