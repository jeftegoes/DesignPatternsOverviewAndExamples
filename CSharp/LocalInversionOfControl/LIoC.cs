namespace LocalInversionOfControl
{
    public class LIoC
    {
        public void AddingNumbers()
        {
            var list = new List<int>();
            var list2 = new List<int>();
            // list.Add(24);
            24.AddTo(list, list2);
        }

        public string ProcessCommand(string opcode)
        {
            // if (opcode == "AND" || opcode == "OR" || opcode == "XOR") { };
            // if (new[] { "AND", "OR", "XOR" }.Contains(opcode)) { };
            // if ("AND OR XOR".Split(' ').Contains(opcode)) { };
            return (opcode.IsOneOf("AND", "OR", "XOR")) ? "Command processed." : "Command don't processed.";
        }

        public string Process(Person person)
        {
            // if (person.Names.Count == 0) { }
            // if (!person.Names.Any()) { }
            return (person.HasSome(p => p.Names).And.HasNo(p => p.Children) ? "Has values." : "Has no values.");
        }
    }
}