using WithBuilder;

var htmlBuilder = new HtmlBuilder("ul");
htmlBuilder.AddChild("li", "hello");
htmlBuilder.AddChild("li", "world");
Console.WriteLine(htmlBuilder.ToString());