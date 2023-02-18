import copy

from address import Address
from person import Person

jefte = Person("Jefté", Address("Av. Sete", "Brazil", "Salvador"))
print(jefte)


brenno = copy.deepcopy(jefte)
brenno.name = "Brenno"
brenno.address.street_address = "Av. Paralela"
print(brenno)
