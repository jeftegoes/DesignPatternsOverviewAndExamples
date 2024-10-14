from builder import Builder
from car import Car


class Director:
    def set_builder(self, builder: Builder):
        self.__builder = builder

    def get_car(self) -> Car:
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        engine = self.__builder.get_engine()
        car.set_engine(engine)

        i = 0
        while i < 4:
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)

            i += 1

        return car
