const Person = require("./person");

class PersonFactory {
  createPerson(name) {
    return new Person(PersonFactory.id++, name);
  }
}

PersonFactory.id = 0;

module.exports = PersonFactory;
