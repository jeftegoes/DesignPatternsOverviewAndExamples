using BankAccountDepositWithdraw;

var bankAccount = new BankAccount();
var bankAccountCommandList = new List<BankAccountCommand>()
{
    new BankAccountCommand(bankAccount, TypeOperation.Deposit, 100),
    new BankAccountCommand(bankAccount, TypeOperation.Withdraw, 1000),
};

Console.WriteLine(bankAccount);

foreach (var bankAccountCommand in bankAccountCommandList)
    bankAccountCommand.Call();

Console.WriteLine(bankAccount);

foreach (var bankAccountCommand in Enumerable.Reverse(bankAccountCommandList))
    bankAccountCommand.Undo();

Console.WriteLine(bankAccount);