from creature_modifier import CreatureModifier


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increasing {self.creature.name} defense.")
            self.creature.defense += 1
        super().handle()