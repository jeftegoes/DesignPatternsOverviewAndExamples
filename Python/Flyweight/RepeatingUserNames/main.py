import random
import string

from user import User
from user_2 import User2


def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for x in range(8)])


users = []

first_names = [random_string() for x in range(100)]
last_names = [random_string() for x in range(100)]

for first in first_names:
    for last in last_names:
        users.append(User(f'{first} {last}'))

u2 = User2('Jim Jones')
u3 = User2('Frank Jones')
print(u2.names)
print(u3.names)
print(User2.strings)

users2 = []

for first in first_names:
    for last in last_names:
        users2.append(User2(f'{first} {last}'))
