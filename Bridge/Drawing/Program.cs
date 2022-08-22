using Drawing;

IRenderer renderer = new RasterRenderer();
var circle = new Circle(renderer, 5);
circle.Draw();
circle.Resize(2);
circle.Draw();