using MoreLinq;

namespace SingletonDatabaseWithDependencyInjection
{
    public class OrdinaryDatabase : IDatabase
    {
        private Dictionary<string, int> capitals;

        public OrdinaryDatabase()
        {
            Console.WriteLine("Initializing Ordinary Database.");
            
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