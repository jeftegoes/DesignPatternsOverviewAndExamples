from person_factory import PersonFactory

person_factory = PersonFactory()

person_1 = person_factory.create_person("Jefté")
print(person_1.id, person_1.name)

person_2 = person_factory.create_person("Brenno")
print(person_2.id, person_2.name)
