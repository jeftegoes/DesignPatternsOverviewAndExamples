const VectorRectangle = require("./vectorRectangle");
const LineToPointAdapter = require("./lineToPointAdapter");

let drawPoint = function (point) {
  process.stdout.write(".");
};

let vectorObjects = [
  new VectorRectangle(1, 1, 10, 10),
  new VectorRectangle(1, 1, 10, 10),
];

let drawPoints = function () {
  for (let vo of vectorObjects)
    for (let line of vo) {
      let adapter = new LineToPointAdapter(line);
      adapter.forEach(drawPoint);
    }
};

drawPoints();
drawPoints();
