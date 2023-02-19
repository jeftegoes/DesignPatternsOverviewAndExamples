from line import Line
from point import Point

line1 = Line(
    Point(3, 3),
    Point(10, 10)
)
line2 = line1.deep_copy()

print(line2.start.x)
print(line2.start.y)
print(line2.end.x)
print(line2.end.y)