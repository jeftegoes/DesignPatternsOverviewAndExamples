from memento import Memento


class BankAccount:
    def __init__(self, balance: int = 0) -> None:
        self.balance = balance

    def deposit(self, amount: int) -> Memento:
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento: Memento) -> None:
        self.balance = memento.balance

    def __str__(self) -> str:
        return f"Balance = {self.balance}"
