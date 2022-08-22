using MagicSquare;

var magicSquareGenerator = new MagicSquareGenerator();

foreach (var firstRow in magicSquareGenerator.Generate(3))
{
    Console.WriteLine();
    foreach (var item in firstRow)
    {
        Console.Write($"{item} > ");
    }
}