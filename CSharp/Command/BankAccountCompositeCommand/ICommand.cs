namespace BankAccountCompositeCommand
{
    public interface ICommand
    {
         void Call();
         void Undo();
    }
}