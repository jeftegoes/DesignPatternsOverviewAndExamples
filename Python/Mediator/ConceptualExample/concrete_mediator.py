from component_1 import Component1
from component_2 import Component2
from mediator import Mediator


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, message: str) -> None:
        if message == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif message == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()
