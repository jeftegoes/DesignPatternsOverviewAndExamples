from component import Component
from concrete_component import ConcreteComponent
from concrete_decorator_a import ConcreteDecoratorA
from concrete_decorator_b import ConcreteDecoratorB


def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")


simple = ConcreteComponent()
print("Client: I've got a simple component:")
client_code(simple)
print("\n")


decorator1 = ConcreteDecoratorA(simple)
decorator2 = ConcreteDecoratorB(decorator1)
print("Client: Now I've got a decorated component:")
client_code(decorator2)
