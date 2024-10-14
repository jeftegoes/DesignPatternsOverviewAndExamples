from action import Action
from bank_account import BankAccount
from bank_account_command import BankAccountCommand
from composite_bank_account_command import CompositeBankAccountCommand
from money_transfer_command import MoneyTransferCommand


def test_composite_deposit():
    ba = BankAccount()
    deposit1 = BankAccountCommand(ba, Action.DEPOSIT, 1000)
    deposit2 = BankAccountCommand(ba, Action.DEPOSIT, 1000)
    composite = CompositeBankAccountCommand([deposit1, deposit2])
    composite.invoke()
    print(ba)
    composite.undo()
    print(ba)

def test_transfer_fail():
    ba1 = BankAccount(100)
    ba2 = BankAccount()

    # composite isn't so good because of failure
    amount = 1000  # try 1000: no transactions should happen
    wc = BankAccountCommand(ba1, Action.WITHDRAW, amount)
    dc = BankAccountCommand(ba2, Action.DEPOSIT, amount)

    transfer = CompositeBankAccountCommand([wc, dc])

    transfer.invoke()
    print('ba1:', ba1, 'ba2:', ba2)  # end up in incorrect state
    transfer.undo()
    print('ba1:', ba1, 'ba2:', ba2)

def test_better_tranfer():
    ba1 = BankAccount(100)
    ba2 = BankAccount()

    amount = 1000

    transfer = MoneyTransferCommand(ba1, ba2, amount)
    transfer.invoke()
    print('ba1:', ba1, 'ba2:', ba2)
    transfer.undo()
    print('ba1:', ba1, 'ba2:', ba2)
    print(transfer.success)

test_composite_deposit()
test_transfer_fail()
test_better_tranfer()