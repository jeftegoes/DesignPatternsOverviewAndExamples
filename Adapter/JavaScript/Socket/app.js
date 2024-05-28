const Socket = require("./socket");
const Adapter = require("./adapter");
const ElectricKettle = require("./electricKettle");

function main() {
  const socket = new Socket();
  const adapter = new Adapter(socket);
  const kettle = new ElectricKettle(adapter);

  kettle.boil();

  return 0;
}

main();
