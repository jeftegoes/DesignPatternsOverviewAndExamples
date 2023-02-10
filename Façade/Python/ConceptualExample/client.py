from facade import Facade


class Client:
    def client_code(self, facade: Facade) -> None:
        print(facade.operation(), end="")
