namespace NullObjectSingleton
{
    public interface ILog
    {
        void Warn();

        public ILog Null => NullLog.Instance;

        private sealed class NullLog : ILog
        {
            private NullLog()
            {

            }

            private static Lazy<NullLog> _instance = new Lazy<NullLog>(() => new NullLog());

            public static ILog Instance => _instance.Value;

            public void Warn()
            {
                Console.WriteLine("Warn singleton.");
            }
        }
    }
}