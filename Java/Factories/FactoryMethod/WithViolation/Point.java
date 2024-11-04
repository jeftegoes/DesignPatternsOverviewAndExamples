public class Point {
    private double x, y;

    public Point(double x, double y, CoordinateSystem coordinateSystem) {
        switch (coordinateSystem) {
            case CoordinateSystem.CARTESIAN -> {
                this.x = x;
                this.y = y;
            }
            case CoordinateSystem.POLAR -> {
                this.x = x * Math.cos(y);
                this.y = x * Math.sin(y);
            }
            default -> throw new AssertionError();
        }
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }
}
