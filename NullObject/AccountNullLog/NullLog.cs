namespace AccountNullLog
{
    public class NullLog : ILog
    {
        public int RecordLimit { get; } = int.MaxValue;

        public int RecordCount { get; set; } = int.MinValue;

        public void LogInfo(string message)
        {
            Console.WriteLine(message);
            ++RecordCount;
        }
    }
}