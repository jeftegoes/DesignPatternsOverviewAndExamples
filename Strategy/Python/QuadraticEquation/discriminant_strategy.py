from abc import ABC


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a: int, b: int, c: int) -> float:
        pass
