from memento import Memento


class BankAccount:
    def __init__(self, balance: int = 0) -> None:
        self.balance = balance
        self.changes: list[Memento] = [Memento(self.balance)]
        self.current: int = 0

    def deposit(self, amount: int) -> Memento:
        self.balance += amount
        memento = Memento(self.balance)
        self.changes.append(memento)
        self.current += 1
        return memento

    def restore(self, memento: Memento) -> None:
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current = len(self.changes)-1

    def undo(self):
        if self.current > 0:
            self.current -= 1
            memento = self.changes[self.current]
            self.balance = memento.balance
            return memento

        return None

    def redo(self):
        if self.current + 1 < len(self.changes):
            self.current += 1
            memento = self.changes[self.current]
            self.balance = memento.balance
            return memento

        return None

    def __str__(self) -> str:
        return f"Balance = {self.balance}"
