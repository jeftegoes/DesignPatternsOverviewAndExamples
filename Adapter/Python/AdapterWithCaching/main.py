from line import Line
from line_to_point_adapter import LineToPointAdapter
from point import Point
from rectangle import Rectangle


def draw_point(p):
    print('.', end='')


def draw(rcs):
    print('Drawing some rectangles...')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
    print('\n')


rs = [
    Rectangle(1, 1, 10, 10),
    Rectangle(3, 3, 6, 6)
]

draw(rs)
draw(rs)

print(hash(Line(Point(1, 1), Point(10, 10))))
