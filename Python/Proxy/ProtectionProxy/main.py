from car_proxy import CarProxy
from driver import Driver

car = CarProxy(Driver('John', 12))
car.drive()
