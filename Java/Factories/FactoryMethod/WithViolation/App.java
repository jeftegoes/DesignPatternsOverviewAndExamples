public class App {
    public static void main(String[] args) {
        Point point = new Point(2, 3, CoordinateSystem.POLAR);
        System.out.println("X: " + point.getX() + " Y: " + point.getY());
    }
}