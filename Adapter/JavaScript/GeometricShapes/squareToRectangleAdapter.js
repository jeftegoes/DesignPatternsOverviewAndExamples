class SquareToRectangleAdapter {
  constructor(square) {
    this.square = square;
  }

  get width() {
    return this.square.side;
  }

  get height() {
    return this.square.side;
  }
}

module.exports = SquareToRectangleAdapter;
