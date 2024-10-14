from brazilian_socket_interface import BrazilianSocketInterface
from european_socket import EuropeanSocket


class BrazilianSocketAdapter(BrazilianSocketInterface):
    def __init__(self, european_socket: EuropeanSocket) -> None:
        self.european_socket = european_socket

    def voltage(self):
        return 110

    def live(self):
        return self.european_socket.live()

    def neutral(self):
        return self.european_socket.neutral()

    def earth(self):
        return self.european_socket.earth()