from subject import Subject


class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Handling request.")