namespace BankAccountCompositeCommand
{
    public class BankAccountCommand : Command
    {
        private readonly BankAccount _bankAccount;
        private readonly TypeOperation _typeOperation;
        private readonly int _amount;
        private bool _succeeded;

        public BankAccountCommand(BankAccount bankAccount, TypeOperation typeOperation, int amount)
        {
            _bankAccount = bankAccount;
            _typeOperation = typeOperation;
            _amount = amount;

        }

        public override void Call()
        {
            switch (_typeOperation)
            {
                case TypeOperation.Deposit:
                    _bankAccount.Deposit(_amount);
                    _succeeded = true;
                    break;
                case TypeOperation.Withdraw:
                    _succeeded = _bankAccount.Withdraw(_amount);
                    break;
                default:
                    break;
            }
        }

        public override void Undo()
        {
            if (!_succeeded) return;

            switch (_typeOperation)
            {
                case TypeOperation.Deposit:
                    _bankAccount.Withdraw(_amount);
                    break;
                case TypeOperation.Withdraw:
                    _bankAccount.Deposit(_amount);
                    break;
                default:
                    break;
            }
        }
    }
}