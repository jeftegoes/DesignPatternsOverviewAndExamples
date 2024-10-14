class Address:
    def __init__(self, street_address: str, suite: str, city: str) -> None:
        self.suite = suite
        self.city = city
        self.street_address = street_address

    def __str__(self) -> str:
        return f"{self.street_address}, Suite #{self.suite}, {self.suite}"
