namespace VectorRaster
{
    public class Line
    {
        private readonly Point _start;
        private readonly Point _end;

        public Line(Point start, Point end)
        {
            _end = end;
            _start = start;
        }
    }
}