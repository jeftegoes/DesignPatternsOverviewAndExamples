using System.Text;

namespace TextFormatting
{
    public class FormattedText
    {
        private readonly string _plainText;
        private bool[] _captilalize;

        public FormattedText(string plainText)
        {
            _plainText = plainText;
            _captilalize = new bool[plainText.Length];
        }

        public void Captalize(int start, int end)
        {
            for (int i = start; i <= end; i++)
                _captilalize[i] = true;
        }

        public override string ToString()
        {
            var stringBuilder = new StringBuilder();
            
            for (int i = 0; i < _plainText.Length; i++)
            {
                var c = _plainText[i];
                stringBuilder.Append(_captilalize[i] ? char.ToUpper(c) : c);
            }

            return stringBuilder.ToString();
        }
    }
}