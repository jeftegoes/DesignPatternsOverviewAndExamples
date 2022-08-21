namespace Facade
{
    public class Generator
    {
        private static readonly Random random = new Random();

        public List<int> Generate(int count)
        {
            return Enumerable.Range(0, count).Select(_ => random.Next(1, 6)).ToList();
        }
    }
}