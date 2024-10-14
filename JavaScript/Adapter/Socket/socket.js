const EuropeanSocketInterface = require("./europeanSocketInterface");

class Socket extends EuropeanSocketInterface {
  voltage() {
    return 230;
  }

  live() {
    return 1;
  }

  neutral() {
    return -1;
  }

  earth() {
    return 0;
  }
}

module.exports = Socket;
