from on_off_state import OffState


class Switch:
    def __init__(self) -> None:
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)
