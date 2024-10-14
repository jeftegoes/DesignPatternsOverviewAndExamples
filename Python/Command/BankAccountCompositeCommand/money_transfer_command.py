from action import Action
from bank_account import BankAccount
from bank_account_command import BankAccountCommand
from composite_bank_account_command import CompositeBankAccountCommand


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acct: BankAccount, to_acct, amount: int):
        super().__init__([
            BankAccountCommand(from_acct,
                               Action.WITHDRAW,
                               amount),
            BankAccountCommand(to_acct,
                               Action.DEPOSIT,
                               amount)])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok
