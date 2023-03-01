from abc import ABC


class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass