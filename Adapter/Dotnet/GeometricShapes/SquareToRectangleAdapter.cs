namespace GeometricShapes
{
    public class SquareToRectangleAdapter : IShape
    {
        private double Width { get; set; }
        private double Height { get; set; }

        public SquareToRectangleAdapter(Square square)
        {
            Width = square.Side;
            Height = square.Side;
        }

        public double CalculateArea()
        {
            return Width * Height;
        }
    }
}