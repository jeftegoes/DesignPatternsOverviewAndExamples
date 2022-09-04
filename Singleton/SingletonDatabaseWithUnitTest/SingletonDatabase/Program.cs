using SingletonDatabase;

var database = Database.Instance;
var city = "Tokyo";
Console.WriteLine($"{city} has population {database.GetPopulation(city)}");

var databaseRecordFinder = new DatabaseRecordFinder();
var names = new[] { "Seoul", "Mexico City" };
int tp = databaseRecordFinder.GetTotalPopulation(names);
Console.WriteLine($"Total population Seoul and Mexico: {tp}");