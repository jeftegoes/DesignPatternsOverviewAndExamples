using SumImplementation;

var listValueContainer = new List<IValueContainer>();
listValueContainer.Add(new SingleValue() { Value = 5 });
listValueContainer.Add(new ManyValues() { 1, 2, 3 });

Console.WriteLine(listValueContainer.Sum());