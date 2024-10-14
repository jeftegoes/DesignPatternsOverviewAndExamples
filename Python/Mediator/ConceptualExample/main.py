# The client code.
from component_1 import Component1
from component_2 import Component2
from concrete_mediator import ConcreteMediator

c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

print("Client triggers operation A.")
c1.do_a()

print("\n", end="")

print("Client triggers operation D.")
c2.do_d()