using System.Text;

namespace TextFormatting
{
    public class BetterFormattedText
    {
        private readonly string _plainText;
        private List<TextRange> _formatting = new List<TextRange>();

        public BetterFormattedText(string plainText)
        {
            _plainText = plainText;
        }

        public TextRange GetRange(int start, int end)
        {
            var range = new TextRange { Start = start, End = end };
            _formatting.Add(range);
            return range;
        }

        public override string ToString()
        {
            var stringBuilder = new StringBuilder();

            for (int i = 0; i < _plainText.Length; i++)
            {
                var c = _plainText[i];
                foreach (var range in _formatting)
                {
                    if (range.Covers(i) && range.Capitalize)
                        c = char.ToUpperInvariant(c);
                }

                stringBuilder.Append(c);
            }

            return stringBuilder.ToString();
        }
    }
}