using System.Collections;

namespace ExampleWithDisposable
{
    public interface IScalar<T> : IEnumerable<T>
    {
        IEnumerator<T> IEnumerable<T>.GetEnumerator()
        {
            yield return (T)this;
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }
}