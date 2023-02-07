using GeometricShapes;

static double CalculateArea(IShape shape)
{
    return shape.CalculateArea();
}

var square = new Square(10);
Console.WriteLine("Area of Square is: {0}", CalculateArea(square));

var squareToRectangleAdapter = new SquareToRectangleAdapter(square);
Console.WriteLine("Area of Rectangle with Adapter is: {0}", CalculateArea(squareToRectangleAdapter));

var squareToCircleAdapter = new SquareToCircleAdapter(square);
Console.WriteLine("Area of circle with Adapter is: {0}", CalculateArea(squareToCircleAdapter));

