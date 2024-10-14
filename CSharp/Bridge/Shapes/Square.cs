namespace Shapes
{
    public class Square : Shape
    {
        private readonly IRenderer _renderer;

        public Square(IRenderer renderer) : base(renderer)
        {
            base.Name = "Square";
            _renderer = renderer;
        }

        public override string ToString()
        {
            return ($"{_renderer.WhatToRenderAs} {base.Name}");
        }
    }
}