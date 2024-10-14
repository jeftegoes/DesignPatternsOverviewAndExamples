namespace BankAccountCompositeCommand
{
    public abstract class Command
    {
        public abstract void Call();
        public abstract void Undo();
        public bool _succeeded;
    }
}