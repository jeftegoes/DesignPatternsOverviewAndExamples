using NullObjectWithIoC;

// var log = new ConsoleLog();
var bankAccount = new BankAccount(null);
bankAccount.Deposit(100);