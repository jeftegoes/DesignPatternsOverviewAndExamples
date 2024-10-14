from bank_account import BankAccount

bank_account = BankAccount(100)
memento_1 = bank_account.deposit(50)
memento_2 = bank_account.deposit(25)
print(bank_account)

bank_account.undo()
print(f"Undo 1: {bank_account}")

bank_account.undo()
print(f"Undo 2: {bank_account}")

bank_account.redo()
print(f"Redo 1: {bank_account}")