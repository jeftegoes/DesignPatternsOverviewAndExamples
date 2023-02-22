from game import Game
from query import Query
from what_to_query import WhatToQuery


class Creature:
    def __init__(self, game: Game, name: str, attack: int, defense: int):
        self.initial_defense = defense
        self.initial_attack = attack
        self.name = name
        self.game = game

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'
