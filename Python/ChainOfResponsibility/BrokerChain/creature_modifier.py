from abc import ABC

from creature import Creature
from game import Game
from query import Query


class CreatureModifier(ABC):
    def __init__(self, game: Game, creature: Creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender, query: Query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)
