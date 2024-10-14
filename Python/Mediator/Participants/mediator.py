from event import Event


class Mediator:
    def __init__(self):
        self.alert = Event()

    def broadcast(self, sender, value: int):
        self.alert(sender, value)