using System.Text;

namespace WithBuilder
{
    public class HtmlElement
    {
        public string Tag, Value;
        public List<HtmlElement> Elements = new List<HtmlElement>();

        private const int identSize = 2;

        public HtmlElement()
        {

        }

        public HtmlElement(string tag, string value)
        {
            Tag = tag;
            Value = value;
        }

        private string ToStringImpl(int indent)
        {
            var sb = new StringBuilder();
            var i = new string(' ', identSize * indent);
            sb.AppendLine($"{i}<{Tag}>");

            if (!string.IsNullOrWhiteSpace(Value))
            {
                sb.Append(new string(' ', identSize * indent + 1));
                sb.AppendLine(Value);
            }

            foreach (var e in Elements)
            {
                sb.Append(e.ToStringImpl(indent + 1));
            }
            sb.AppendLine($"{i}</{Tag}>");

            return sb.ToString();
        }

        public override string ToString()
        {
            return ToStringImpl(0);
        }
    }
}