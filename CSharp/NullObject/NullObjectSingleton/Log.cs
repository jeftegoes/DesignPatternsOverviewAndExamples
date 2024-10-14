namespace NullObjectSingleton
{
    public class Log : ILog
    {
        public void Warn()
        {
            Console.WriteLine("Warn");
        }
    }
}