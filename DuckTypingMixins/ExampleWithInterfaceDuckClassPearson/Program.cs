using ExampleWithInterfaceDuckClassPearson;

void DoThingsLikeDuck(dynamic anything)
{
    if (anything != null)
    {
        anything.Walk();
        anything.Swim();
        anything.Quack();
    }
}

var person = new Person();

var personImitatingADuck = person as IDuck;

var isPerson = person is IDuck;

Console.WriteLine("Person is a Duck? {0}", isPerson);
Console.WriteLine("Person Imitating a Duck? {0}", personImitatingADuck != null);

if (isPerson || personImitatingADuck != null)
{
    personImitatingADuck.Walk();
    personImitatingADuck.Swim();
    personImitatingADuck.Quack();
}

DoThingsLikeDuck(person);