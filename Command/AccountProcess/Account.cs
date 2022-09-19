namespace AccountProcess
{
    public class Account
    {
        public int Balance { get; set; }

        public void Process(Command c)
        {
            switch (c.TheAction)
            {
                case TypeOperation.Deposit:
                    Balance += c.Amount;
                    c.Success = true;
                    break;
                case TypeOperation.Withdraw:
                    c.Success = Balance >= c.Amount;
                    if (c.Success) Balance -= c.Amount;
                    break;
                default:
                    throw new ArgumentOutOfRangeException();
            }
        }
    }
}