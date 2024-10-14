from address import Address


class Person:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} lives at {self.address}"
