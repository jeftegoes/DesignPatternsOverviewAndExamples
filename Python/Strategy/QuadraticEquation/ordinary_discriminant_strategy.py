from discriminant_strategy import DiscriminantStrategy


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a: int, b: int, c: int) -> float:
        return b*b - 4*a*c
