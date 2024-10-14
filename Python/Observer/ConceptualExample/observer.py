from abc import ABC, abstractmethod

from subject import Subject


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass