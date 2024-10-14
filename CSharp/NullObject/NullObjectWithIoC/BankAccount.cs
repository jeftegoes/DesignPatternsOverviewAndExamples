namespace NullObjectWithIoC
{
    public class BankAccount
    {
        private readonly ILog _log;
        private int balance;

        public BankAccount(ILog log)
        {
            _log = log;
        }

        public void Deposit(int amount)
        {
            balance += amount;
            _log?.Info($"Deposited {amount}, balance is now {balance}");
        }
    }
}