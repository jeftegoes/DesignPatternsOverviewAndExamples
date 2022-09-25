namespace CqrsEventSourcing
{
    public class Person
    {
        private int _age;
        private readonly EventBroker _broker;

        public Person(EventBroker broker)
        {
            _broker = broker;
            _broker.Commands += BrokerOnCommands;
            _broker.Queries += BrokerOnQueries;
        }

        private void BrokerOnQueries(object sender, Query query)
        {
            var ac = query as AgeQuery;
            if (ac != null && ac.Target == this)
            {
                ac.Result = _age;
            }
        }

        private void BrokerOnCommands(object sender, Command command)
        {
            var cac = command as ChangeAgeCommand;
            if (cac != null && cac.Target == this)
            {
                if (cac.Register)
                    _broker.AllEvents.Add(new AgeChangedEvent(this, _age, cac.Age));

                _age = cac.Age;
            }
        }
    }
}