import copy

from point import Point


class Line:
    def __init__(self, start: Point = Point(), end: Point = Point()) -> None:
        self.start = start
        self.end = end

    def deep_copy(self):
        new_start = Point(self.start.x, self.start.y)
        new_end = Point(self.end.x, self.end.y)
        return Line(new_start, new_end)
