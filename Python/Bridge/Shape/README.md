# Bridge Coding

- You are given an example of an inheritance hierarchy which results in Cartesian-product duplication.

- Please refactor this hierarchy, giving the base class `Shape` a constructor that takes an interface `Renderer` defined as:

```
class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None
```

- As well as `VectorRenderer` and `RasterRenderer` classes.
- Each inheritor of the `Shape` abstract class should have a constructor that takes a `Renderer` such that, subsequently, each constructed object's `__str__()` operates correctly, for example, `str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels"`.
