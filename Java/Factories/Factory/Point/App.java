public class App {
    public static void main(String[] args) {
        Point point = Point.Factory.newPolarPoint(2, 3);
        System.out.println("X: " + point.getX() + " Y: " + point.getY());
    }
}