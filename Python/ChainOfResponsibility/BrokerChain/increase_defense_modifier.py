from creature_modifier import CreatureModifier
from what_to_query import WhatToQuery


class IncreaseDefenseModifier(CreatureModifier):

    def handle(self, sender, query):
        if (sender.name == self.creature.name and
                query.what_to_query == WhatToQuery.DEFENSE):
            query.value += 3
