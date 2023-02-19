using Autofac;
using DrawingWithIoCAutoFac;

var cb = new ContainerBuilder();
cb.RegisterType<RasterRenderer>().As<IRenderer>().SingleInstance();
cb.Register((c, p) => new Circle(c.Resolve<IRenderer>(), p.Positional<float>(0)));

using (var c = cb.Build())
{
    var circle = c.Resolve<Circle>(new PositionalParameter(0, 5.0f));
    circle.Draw();
    circle.Resize(2.0f);
    circle.Draw();
}