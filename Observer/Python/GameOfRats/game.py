from event import Event


class Game:
    def __init__(self):
        self.rat_enters = Event()
        self.rat_dies = Event()
        self.notify_rat = Event()