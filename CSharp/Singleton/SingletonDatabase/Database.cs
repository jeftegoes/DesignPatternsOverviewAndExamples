using MoreLinq;

namespace SingletonDatabase
{
    public class Database : IDatabase
    {
        private Dictionary<string, int> capitals;
        private static Lazy<Database> _instance =
            new Lazy<Database>(() => new Database());

        public static Database Instance = _instance.Value;

        public Database()
        {
            Console.WriteLine("Initializing database.");
            capitals = File.ReadAllLines("capitals.txt")
                .Batch(2)
                .ToDictionary(
                    list => list.ElementAt(0).Trim(),
                    list => int.Parse(list.ElementAt(1))
                );
        }

        public int GetPopulation(string name)
        {
            return capitals[name];
        }
    }
}