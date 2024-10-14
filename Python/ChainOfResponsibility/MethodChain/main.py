from creature import Creature
from creature_modifier import CreatureModifier
from double_attack_modifier import DoubleAttackModifier
from increase_defense_modifier import IncreaseDefenseModifier
from no_bonuses_modifier import NoBonusesModifier

goblin = Creature("Goblin", 1, 1)
print(goblin)

creature_modifier = CreatureModifier(goblin)
creature_modifier.add_modifier(NoBonusesModifier(goblin))
creature_modifier.add_modifier(DoubleAttackModifier(goblin))
creature_modifier.add_modifier(DoubleAttackModifier(goblin))
creature_modifier.add_modifier(IncreaseDefenseModifier(goblin))
creature_modifier.handle()  # apply modifiers
print(goblin)
