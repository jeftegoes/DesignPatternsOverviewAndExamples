from creature_modifier import CreatureModifier


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print("No bonuses for you.")
