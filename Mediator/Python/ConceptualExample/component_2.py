from base_component import BaseComponent


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify("C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify("D")