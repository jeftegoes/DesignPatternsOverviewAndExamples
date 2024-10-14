const Square = require("./square");
const SquareToRectangleAdapter = require("./squareToRectangleAdapter");

function area(rectangle) {
  return rectangle.width * rectangle.height;
}

let sq = new Square(11);
let adapter = new SquareToRectangleAdapter(sq);
console.log(area(adapter));
