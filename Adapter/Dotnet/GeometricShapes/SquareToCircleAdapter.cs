namespace GeometricShapes
{
    public class SquareToCircleAdapter : IShape
    {
        public double Radius { get; set; }

        public SquareToCircleAdapter(Square square)
        {
            Radius = square.Side;
        }

        public double CalculateArea()
        {
            return Math.PI * Math.Pow(Radius, 2);
        }
    }
}