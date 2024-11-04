public class App {
    public static void main(String[] args) {
        PersonFactory personFactory = new PersonFactory();
        Person person1 = personFactory.createPerson("Jefté");
        Person person2 = personFactory.createPerson("Brenno");

        System.out.println(person1);
        System.out.println(person2);
    }
}