namespace HelloWorldSetence
{
    public class Sentence
    {
        private string[] _words;
        private Dictionary<int, WordToken> _tokens = new Dictionary<int, WordToken>();

        public Sentence(string plainText)
        {
            _words = plainText.Split(' ');
        }

        public WordToken this[int index]
        {
            get
            {
                WordToken wt = new WordToken();
                _tokens.Add(index, wt);

                return _tokens[index];
            }
        }

        public override string ToString()
        {
            var list = new List<string>();

            for (var i = 0; i < _words.Length; i++)
            {
                var w = _words[i];

                if (_tokens.ContainsKey(i) && _tokens[i].Capitalize)
                    w = w.ToUpperInvariant();

                list.Add(w);
            }

            return string.Join(" ", list);
        }
    }
}