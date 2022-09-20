using LocalInversionOfControl;

var lioc = new LIoC();

lioc.AddingNumbers();
Console.WriteLine(lioc.ProcessCommand("XOR"));
Console.WriteLine(lioc.Process(new Person()));