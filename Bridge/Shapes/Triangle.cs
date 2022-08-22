namespace Shapes
{
    public class Triangle : Shape
    {
        private readonly IRenderer _renderer;

        public Triangle(IRenderer renderer) : base(renderer)
        {
            base.Name = "Triangle";
            _renderer = renderer;
        }

        public override string ToString()
        {
            return ($"{_renderer.WhatToRenderAs} {base.Name}");
        }
    }
}