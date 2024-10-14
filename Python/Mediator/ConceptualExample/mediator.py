from abc import ABC


class Mediator(ABC):
    def notify(self, message: str) -> None:
        pass