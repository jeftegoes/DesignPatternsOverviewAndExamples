import cmath

from discriminant_strategy import DiscriminantStrategy


class QuadraticEquationSolver:
    def __init__(self, strategy: DiscriminantStrategy) -> None:
        self.strategy = strategy

    def solve(self, a: int, b: int, c: int):
        """ Returns a pair of complex (!) values """
        disc = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        root_disc = cmath.sqrt(disc)
        return (
            (-b + root_disc) / (2 * a),
            (-b - root_disc) / (2 * a)
        )
