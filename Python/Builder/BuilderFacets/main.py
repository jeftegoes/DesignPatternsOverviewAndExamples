from person_builder import PersonBuilder

person_builder = PersonBuilder()
person = person_builder\
    .lives.at("Bahia").in_city("Salvador").with_postcode("40020-901")\
    .works.at("Myself").as_a("Software Engineer").earning(121300)\
    .build()

print(person)

person2 = PersonBuilder().build()
print(person2)
