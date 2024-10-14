from discriminant_strategy import DiscriminantStrategy


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a: int, b: int, c: int) -> float:
        result = b*b-4*a*c
        return result if result >= 0 else float('nan')
