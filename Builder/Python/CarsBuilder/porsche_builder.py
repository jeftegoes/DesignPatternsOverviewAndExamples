from body import Body
from builder import Builder
from engine import Engine
from wheel import Wheel


class PorscheBuilder(Builder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 800
        return engine

    def get_body(self):
        body = Body()
        body.shape = "Coupe"
        return body
