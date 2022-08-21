namespace Facade
{
    public class MagicSquareGenerator
    {
        public List<List<int>> Generate(int size)
        {
            var list = new List<List<int>>();
            var generated = new Generator().Generate(size);

            // Console.WriteLine("Generated: {0}", generated.Count());
            // foreach (var item in generated)
            // {
            //     Console.Write($"{item}, ");
            // }
            // Console.WriteLine();
            // Console.WriteLine("--------------");

            for (int i = 0; i < size; i++)
            {
                list.Add(generated);
            }

            var splitter = new Splitter();
            var splited = splitter.Split(list);

            var verifier = new Verifier().Verify(splited);
            // Console.WriteLine("Valid? {0}", verifier);

            if (verifier == false)
                Generate(size);

            // if (verifier == true)
            // {
            //     foreach (var firstRow in splited)
            //     {
            //         Console.WriteLine();
            //         foreach (var item in firstRow)
            //         {
            //             Console.Write($"{item} > ");
            //         }
            //     }
            // }

            return splited;
        }
    }
}