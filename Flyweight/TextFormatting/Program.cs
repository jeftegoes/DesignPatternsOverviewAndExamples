using TextFormatting;

const string text = "Hello world, this is my text editor.";

var formattedText = new FormattedText(text);
formattedText.Captalize(10, 15);
Console.WriteLine(formattedText);

var betterFormattedText = new BetterFormattedText(text);
betterFormattedText.GetRange(10, 15).Capitalize = true;
Console.WriteLine(betterFormattedText);