using CqrsEventSourcing;

var eventBroker = new EventBroker();
var person = new Person(eventBroker);
eventBroker.Command(new ChangeAgeCommand(person, 123));
eventBroker.Command(new ChangeAgeCommand(person, 321));

foreach (var e in eventBroker.AllEvents)
{
    Console.WriteLine(e); ;
}

int age = eventBroker.Query<int>(new AgeQuery { Target = person });
Console.WriteLine(age);

eventBroker.UndoLast();

foreach (var e in eventBroker.AllEvents)
{
    Console.WriteLine(e);
}

age = eventBroker.Query<int>(new AgeQuery { Target = person });
Console.WriteLine(age);