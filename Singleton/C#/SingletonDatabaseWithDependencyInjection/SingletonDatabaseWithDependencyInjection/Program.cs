using Microsoft.Extensions.DependencyInjection;
using SingletonDatabaseWithDependencyInjection;

var serviceCollection = new ServiceCollection();
serviceCollection.AddSingleton<IDatabase, OrdinaryDatabase>();
serviceCollection.AddScoped<ConfigurableRecordFinder>();

var buildServiceProvider = serviceCollection.BuildServiceProvider();
var databaseRecordFinder = buildServiceProvider.GetService<ConfigurableRecordFinder>();

var names = new[] { "Seoul", "Mexico City" };
int tp = databaseRecordFinder.GetTotalPopulation(names);
Console.WriteLine($"Total population Seoul and Mexico: {tp}");