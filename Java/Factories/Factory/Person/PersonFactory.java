public class PersonFactory {
    private int id = 0;

    public Person createPerson(String name) {
        return new Person(id++, name);
    }
}