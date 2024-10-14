from client import Client
from facade import Facade
from subsystem_1 import Subsystem1
from subsystem_2 import Subsystem2

subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
facade = Facade(subsystem1, subsystem2)
client = Client()
client.client_code(facade)
