from creature import Creature
from double_attack_modifier import DoubleAttackModifier
from game import Game
from increase_defense_modifier import IncreaseDefenseModifier

game = Game()
goblin = Creature(game, 'Strong Goblin', 2, 2)
print(goblin)

with DoubleAttackModifier(game, goblin):
    print(goblin)
    with IncreaseDefenseModifier(game, goblin):
        print(goblin)

print(goblin)
