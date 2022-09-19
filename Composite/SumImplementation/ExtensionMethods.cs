namespace SumImplementation
{
    public static class ExtensionMethods
    {
        public static int Sum(this List<IValueContainer> containers)
        {
            int result = 0;

            foreach (var c in containers)
                foreach (var i in c)
                {
                    result += i;
                }

            return result;
        }
    }
}