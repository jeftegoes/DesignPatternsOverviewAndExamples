from creature_modifier import CreatureModifier


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack.")
        self.creature.attack *= 2
        super().handle()
