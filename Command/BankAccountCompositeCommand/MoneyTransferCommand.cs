namespace BankAccountCompositeCommand
{
    public class MoneyTransferCommand : CompositeBankAccountCommand
    {
        public MoneyTransferCommand(BankAccount from,
                                    BankAccount to,
                                    int amount)
        {
            AddRange(new[]
            {
                new BankAccountCommand(from, TypeOperation.Withdraw, amount),
                new BankAccountCommand(to, TypeOperation.Deposit, amount)
            });
        }

        public override void Call()
        {
            bool ok = true;
            foreach (var cmd in this)
            {
                if (ok)
                {
                    cmd.Call();
                    ok = cmd._succeeded;
                }
                else
                {
                    cmd._succeeded = false;
                }
            }
        }
    }
}