namespace PerThreadSingleton
{
    public sealed class PerThread
    {
        private static ThreadLocal<PerThread> threadInstance = new ThreadLocal<PerThread>(()
            => new PerThread());

        public static PerThread Instance => threadInstance.Value;

        public int Id;

        private PerThread()
        {
            Id = Thread.CurrentThread.ManagedThreadId;
        }
    }
}