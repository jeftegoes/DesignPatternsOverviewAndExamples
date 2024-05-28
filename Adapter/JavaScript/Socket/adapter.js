const USASocketInterface = require("./usaSocketInterface");

class Adapter extends USASocketInterface {
  constructor(socket) {
    super();
    this._socket = socket;
  }

  voltage() {
    return 110;
  }

  live() {
    return this._socket.live();
  }

  neutral() {
    return this._socket.neutral();
  }
}

module.exports = Adapter;
