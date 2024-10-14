from addition_expression import AdditionExpression
from double_expression import DoubleExpression

addition_expression = AdditionExpression(DoubleExpression(
    1), AdditionExpression(DoubleExpression(2), DoubleExpression(3)))

buffer = []
addition_expression.print(buffer)
print(''.join(buffer), '=', addition_expression.eval())
