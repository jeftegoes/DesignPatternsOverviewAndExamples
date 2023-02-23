from strategy import Strategy


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: list) -> list:
        return reversed(sorted(data))
