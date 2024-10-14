from bank_account import BankAccount

bank_account = BankAccount(100)
memento_1 = bank_account.deposit(50)
memento_2 = bank_account.deposit(25)
memento_3 = bank_account.deposit(10)
print(bank_account)

bank_account.restore(memento_1)
print(bank_account)

bank_account.restore(memento_2)
print(bank_account)
