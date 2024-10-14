using Microsoft.Extensions.DependencyInjection;
using NullObjectWithIoC;


var collection = new ServiceCollection();
collection.AddScoped<ILog, ConsoleLog>();
collection.AddScoped<BankAccount>();

var provider = collection.BuildServiceProvider();
var bankAccount = provider.GetService<BankAccount>();
bankAccount.Deposit(100);