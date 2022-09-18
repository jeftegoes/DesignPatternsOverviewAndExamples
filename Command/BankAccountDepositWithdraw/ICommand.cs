namespace BankAccountDepositWithdraw
{
    public interface ICommand
    {
         void Call();
         void Undo();
    }
}