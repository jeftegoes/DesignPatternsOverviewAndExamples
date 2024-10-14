from random import randrange

from observer import Observer
from subject import Subject


class ConcreteSubject(Subject):
    _state: int = None
    _observer: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observer.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observer.remove(observer)

    def notify(self) -> None:
        print("Subject: Notify observers...")
        for observer in self._observer:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()
