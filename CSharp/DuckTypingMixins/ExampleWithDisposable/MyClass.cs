namespace ExampleWithDisposable
{
    public class MyClass : IScalar<MyClass>
    {
        public override string ToString()
        {
            return "MyClass";
        }
    }
}