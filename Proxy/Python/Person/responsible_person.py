from person import Person


class ResponsiblePerson:
    def __init__(self, person: Person):
        self.person = person

    @property
    def age(self):
        return self.person.age

    @age.setter
    def age(self, value):
        self.person.age = value

    def drink(self):
        if self.person.age >= 18:
            return self.person.drink()

        return 'too young'

    def drive(self):
        if self.person.age >= 16:
            return self.person.drive()
        return 'too young'

    def drink_and_drive(self):
        return 'dead'
