using SingletonDatabase;

var database = Database.Instance;
var city = "Tokyo";
Console.WriteLine($"{city} has population {database.GetPopulation(city)}");