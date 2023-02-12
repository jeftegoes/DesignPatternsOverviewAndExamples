namespace WithFluentBuilder
{
    public class HtmlBuilder
    {
        private readonly string _rootName;
        HtmlElement root = new HtmlElement();

        public HtmlBuilder(string rootName)
        {
            _rootName = rootName;
            root.Tag = rootName;
        }

        public HtmlBuilder AddChild(string tag, string value)
        {
            var e = new HtmlElement(tag, value);
            root.Elements.Add(e);
            return this;
        }

        public override string ToString()
        {
            return root.ToString();
        }

        public void Clear()
        {
            root = new HtmlElement { Tag = _rootName };
        }
    }
}