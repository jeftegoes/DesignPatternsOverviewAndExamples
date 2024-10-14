from mediator import Mediator


class BaseComponent:
    def __init__(self, mediator: Mediator = None) -> None:
        self.mediator = mediator