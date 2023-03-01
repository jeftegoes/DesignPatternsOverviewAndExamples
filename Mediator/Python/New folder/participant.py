from mediator import Mediator


class Participant:
    def __init__(self, mediator: Mediator):
        self.value = 0
        self.mediator = mediator
        mediator.alert.append(self.mediator_alert)

    def mediator_alert(self, sender, value: int):
        if sender != self:
            self.value += value

    def say(self, value):
        self.mediator.broadcast(self, value)