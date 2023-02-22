from event import Event


class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)
