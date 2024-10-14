class ElectricKettle {
  constructor(power) {
    this._power = power;
  }

  boil() {
    if (this._power.voltage() > 110) {
      console.log("Kettle on fire!");
    } else {
      if (this._power.live() === 1 && this._power.neutral() === -1) {
        console.log("Coffee time!");
      } else {
        console.log("No power.");
      }
    }
  }
}

module.exports = ElectricKettle;
