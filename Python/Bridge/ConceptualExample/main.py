from abstraction import Abstraction
from concrete_implementation_a import ConcreteImplementationA
from concrete_implementation_b import ConcreteImplementationB
from extended_abstraction import ExtendedAbstraction


def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end="")


implementation = ConcreteImplementationA()
abstraction = Abstraction(implementation)
client_code(abstraction)

print("\n")

implementation = ConcreteImplementationB()
abstraction = ExtendedAbstraction(implementation)
client_code(abstraction)
