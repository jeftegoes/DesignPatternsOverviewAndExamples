from brazilian_socket import BrazilianSocketAdapter
from electric_kettle import ElectricKettle
from european_socket import EuropeanSocket

european_socket = EuropeanSocket()
brazilianSocketAdapter = BrazilianSocketAdapter(european_socket)
kettle = ElectricKettle(brazilianSocketAdapter)

kettle.boil()