namespace AmbientalContext
{
    public class Wall
    {
        public Point Start, End;
        public int Height;
        public const int UseAmbient = Int32.MinValue;

        public Wall(Point start, Point end)
        {
            Start = start;
            End = end;
            Height = BuildingContext.Current.WallHeight;
        }

        public override string ToString()
        {
            return $"{nameof(Start)}: {Start}, {nameof(End)}: {End}, " +
                   $"{nameof(Height)}: {Height}";
        }
    }
}