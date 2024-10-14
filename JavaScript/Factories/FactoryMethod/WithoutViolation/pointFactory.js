const Point = require("./point");

class PointFactory {
  newCartesianPoint(x, y) {
    return new Point(x, y);
  }

  static newPolarPoint(rho, theta) {
    return new Point(rho * Math.cos(theta), rho * Math.sin(theta));
  }
} 

module.exports = PointFactory;
