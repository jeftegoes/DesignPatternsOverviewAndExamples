from addition_expression import AdditionExpression
from double_expression import DoubleExpression
from expression_evaluator import ExpressionEvaluator
from expression_printer import ExpressionPrinter

# represents 1+(2+3)
e = AdditionExpression(
    DoubleExpression(1),
    AdditionExpression(
        DoubleExpression(2),
        DoubleExpression(3)
    )
)
printer = ExpressionPrinter()
printer.visit(e)

evaluator = ExpressionEvaluator()
evaluator.visit(e)

print(f'{printer} = {evaluator.value}')
