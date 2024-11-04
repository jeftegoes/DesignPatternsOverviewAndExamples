const PersonFactory = require("./personFactory");

let pf = new PersonFactory();

let p1 = pf.createPerson("Jefté");
console.log(p1.id);

let p2 = pf.createPerson("Brenno");
console.log(p2.id);