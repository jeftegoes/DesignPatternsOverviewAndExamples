namespace RepeatingUserNames
{
    public class User2
    {
        private readonly List<string> strings = new List<string>();

        private int[] names;

        public string FullName => string.Join(" ", names);

        public User2(string fullName)
        {
            int getOrAdd(string s)
            {
                int idx = strings.IndexOf(s);

                if (idx != -1)
                    return idx;
                else
                {
                    strings.Add(s);
                    return strings.Count - 1;
                }
            }

            names = fullName.Split(' ').Select(getOrAdd).ToArray();
        }
    }
}