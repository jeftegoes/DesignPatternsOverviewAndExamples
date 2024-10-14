class Person:
    def __init__(self) -> None:
        print("Creaing and instance of Person")
        # address
        self.street_address: str = None
        self.postcode: str = None
        self.city: str = None
        # employment info
        self.company_name: str = None
        self.position: int = None
        self.annual_income: float = None

    def __str__(self) -> str:
        return f"Address: {self.street_address}, {self.postcode}, {self.city}\nEmployed at {self.company_name} as a {self.postcode} earning {self.annual_income}"
