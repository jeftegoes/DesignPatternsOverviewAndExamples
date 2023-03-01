from mediator import Mediator
from participant import Participant

m = Mediator()
p1 = Participant(m)
p2 = Participant(m)

print(p1.value)
print(p2.value)

p1.say(2)

print(p1.value)
print(p2.value)

p2.say(4)

print(p1.value)
print(p2.value)