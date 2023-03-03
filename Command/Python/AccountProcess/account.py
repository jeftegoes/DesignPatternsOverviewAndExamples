from action import Action
from command import Command


class Account:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def process(self, command: Command):
        if command.action == Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == Action.WITHDRAW:
            command.success = self.balance >= command.amount
            if command.success:
                self.balance -= command.amount
