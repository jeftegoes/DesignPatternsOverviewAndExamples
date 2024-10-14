class Creature:
    def __init__(self, name: str, attack: int, defense: int) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self) -> str:
        return f"{self.name} ({self.attack}/{self.defense})."
