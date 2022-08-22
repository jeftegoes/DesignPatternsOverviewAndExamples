namespace Shapes
{
    public abstract class Shape
    {
        public string Name { get; set; }
        private readonly IRenderer _renderer;

        public Shape(IRenderer renderer)
        {
            _renderer = renderer;
        }
    }
}