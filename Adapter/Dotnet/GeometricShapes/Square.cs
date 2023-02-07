namespace GeometricShapes
{
    public class Square : IShape
    {
        public double Side { get; private set; }

        public Square(double side)
        {
            Side = side;
        }

        public double CalculateArea()
        {
            return Side * Side;
        }
    }
}