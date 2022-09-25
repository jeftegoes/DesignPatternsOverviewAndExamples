namespace CqrsEventSourcing
{
    public class EventBroker
    {
        public IList<Event> AllEvents = new List<Event>();
        public event EventHandler<Command> Commands;
        public event EventHandler<Query> Queries;

        public void Command(Command command)
        {
            Commands.Invoke(this, command);
        }

        public T Query<T>(Query query)
        {
            Queries?.Invoke(this, query);

            return (T)query.Result;
        }

        public void UndoLast()
        {
            var e = AllEvents.LastOrDefault();
            var ac = e as AgeChangedEvent;
            if (ac != null)
            {
                Command(new ChangeAgeCommand(ac.Target, ac.OldValue) { Register = false });
                AllEvents.Remove(e);
            }
        }
    }
}