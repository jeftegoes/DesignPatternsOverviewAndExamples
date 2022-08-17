using WithFluentBuilder;

var htmlBuilder = new HtmlBuilder("ul");
htmlBuilder.AddChild("li", "hello").AddChild("li", "world");
Console.WriteLine(htmlBuilder.ToString());