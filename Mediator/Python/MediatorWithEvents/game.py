from event import Event


class Game:
    def __init__(self):
        self.events = Event()

    def fire(self, args):
        self.events(args)