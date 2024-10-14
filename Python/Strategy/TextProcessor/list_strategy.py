from abc import ABC, abstractmethod


class ListStrategy(ABC):
    def start(self, buffer: list[str]):
        pass

    def end(self, buffer: list[str]):
        pass

    def add_list_item(self, buffer: list[str], item: str):
        pass
