from coordinate_system import CoordinateSystem
from point_intersect import PointIntersect
from point_intersect_factory import PointIntersectFactory

p1 = PointIntersect(2, 3, CoordinateSystem.CARTESIAN)
p2 = PointIntersectFactory.new_cartesian_point(1, 2)
print(p1, p2)
