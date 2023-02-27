from abc import ABC


class State(ABC):
    def on(self, switch):
        print("Light is already on.")

    def off(self, switch):
        print("Light is already off.")
