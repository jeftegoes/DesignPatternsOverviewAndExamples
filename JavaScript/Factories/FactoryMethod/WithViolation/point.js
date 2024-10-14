class Point {
  constructor(a, b, cs = CoordinateSystem.CARTESIAN) {
    switch (cs) {
      case CoordinateSystem.CARTESIAN:
        this.x = a;
        this.y = b;
        break;
      case CoordinateSystem.POLAR:
        this.x = a * Math.cos(b);
        this.y = a * Math.sin(b);
        break;
    }
  }
}

module.exports = Point;
