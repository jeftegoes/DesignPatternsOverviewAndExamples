from state import State


class OnState(State):
    def __init__(self) -> None:
        print("Light turned on.")

    def off(self, switch):
        print("Turning light off...")
        switch.state = OffState()

class OffState(State):
    def __init__(self) -> None:
        print("Light turned off.")

    def on(self, switch):
        print("Turning light on...")
        switch.state = OnState()
