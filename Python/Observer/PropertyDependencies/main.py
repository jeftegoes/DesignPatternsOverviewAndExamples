from person import Person
from traffic_authority import TrafficAuthority


def person_changed(name, value):
    if name == 'can_vote':
        print(f'Voting status changed to {value}')


person = Person()
person.property_changed.append(
    person_changed
)

traffic_authority = TrafficAuthority(person)
for age in range(14, 20):
    print(f"Setting age to {age}")
    person.age = age
