from subsystem_1 import Subsystem1
from subsystem_2 import Subsystem2


class Facade:
    def __init__(self, subsystem_1: Subsystem1, subsystem_2: Subsystem2) -> None:
        self._subsystem_1 = subsystem_1
        self._subsystem_2 = subsystem_2

    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem_1.operation1())
        results.append(self._subsystem_2.operation1())

        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem_1.operation_n())
        results.append(self._subsystem_2.operation_z())

        return "\n".join(results)
