using MoreLinq;

namespace SingletonDatabaseWithDependencyInjection
{
    public class Database : IDatabase
    {
        private Dictionary<string, int> capitals;
        private static Lazy<Database> _instance =
            new Lazy<Database>(() => new Database());
        private static int instanceCount = 0;

        public static Database Instance = _instance.Value;
        public static int Count => instanceCount;

        private Database()
        {
            instanceCount++;
            Console.WriteLine("Initializing Singleton Database.");
            var fileInfo = new FileInfo(typeof(IDatabase).Assembly.Location).DirectoryName;

            capitals = File.ReadAllLines(Path.Combine(fileInfo, "capitals.txt"))
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