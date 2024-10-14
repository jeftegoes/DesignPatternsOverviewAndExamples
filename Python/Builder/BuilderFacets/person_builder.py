from person import Person


class PersonBuilder:
    def __init__(self, person: Person = None) -> None:
        if (person is None):
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)

    def at(self, street_address: str):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode: str):
        self.person.postcode = postcode
        return self

    def in_city(self, city: str):
        self.person.city = city
        return self

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person = None) -> None:
        super().__init__(person)

    def at(self, company_name: str):
        self.person.company_name = company_name
        return self

    def as_a(self, position: str):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self
