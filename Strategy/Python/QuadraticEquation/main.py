from ordinary_discriminant_strategy import OrdinaryDiscriminantStrategy
from quadratic_equation_solver import QuadraticEquationSolver
from real_discriminant_strategy import RealDiscriminantStrategy

strategy = OrdinaryDiscriminantStrategy()
solver = QuadraticEquationSolver(strategy)
results = solver.solve(1, 10, 16)
print(results)

strategy = RealDiscriminantStrategy()
solver = QuadraticEquationSolver(strategy)
results = solver.solve(1, 10, 16)
print(results)

strategy = OrdinaryDiscriminantStrategy()
solver = QuadraticEquationSolver(strategy)
results = solver.solve(1, 4, 5)
print(results)

strategy = RealDiscriminantStrategy()
solver = QuadraticEquationSolver(strategy)
results = solver.solve(1, 4, 5)
print(results)
