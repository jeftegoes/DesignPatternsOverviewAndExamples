from address import Address


class Employee:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} work at {self.address}"
