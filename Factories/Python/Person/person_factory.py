from person import Person


class PersonFactory:

    ID_COUNTER = 0

    def create_person(self, name) -> Person:
        person = Person(self.ID_COUNTER, name)
        self.ID_COUNTER += 1
        return person
