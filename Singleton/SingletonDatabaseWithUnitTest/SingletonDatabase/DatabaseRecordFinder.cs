namespace SingletonDatabase
{
    public class DatabaseRecordFinder
    {
        public int GetTotalPopulation(IEnumerable<string> names)
        {
            int result = 0;
            foreach (var name in names)
                result += Database.Instance.GetPopulation(name);

            return result;
        }
    }
}