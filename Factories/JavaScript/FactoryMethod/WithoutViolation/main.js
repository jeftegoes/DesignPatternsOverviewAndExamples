const Point = require("./point");
const PointFactory = require("./pointFactory");
const CoordinateSystem = require("./coordinateSystem");

let p1 = new Point(2, 3);
console.log(p1);

let p2 = PointFactory.newPolarPoint(2, 3);
console.log(p2);

// This line will not work if newCartesianPoint is static!
// let p3 = Point.factory.newCartesianPoint(2, 3);
// console.log(p3);
