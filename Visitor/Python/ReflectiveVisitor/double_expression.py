from expression import Expression


class DoubleExpression(Expression):
    def __init__(self, value: int) -> None:
        self.value = value
