using PerThreadSingleton;

var t1 = Task.Factory.StartNew(() =>
{
    Console.WriteLine("t1: {0}", PerThread.Instance.Id);
});

var t2 = Task.Factory.StartNew(() =>
{
    Console.WriteLine("t2: {0}", PerThread.Instance.Id);
    Console.WriteLine("t2: {0}", PerThread.Instance.Id);
});

Task.WaitAll(t1, t2);