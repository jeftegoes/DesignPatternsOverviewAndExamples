namespace Facade
{
    public class MagicSquareGenerator
    {
        public List<List<int>> Generate(int size)
        {
            var possibleSquareMagic = new List<List<int>>();
            var generatedNumbers = new Generator().Generate(size);

            for (int i = 0; i < size; i++)
                possibleSquareMagic.Add(generatedNumbers);

            var splited = new Splitter().Split(possibleSquareMagic);
            var isMagicSquare = new Verifier().Verify(splited);

            if (isMagicSquare == false)
                return Generate(size);

            return splited;
        }
    }
}