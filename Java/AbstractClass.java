//Abstract classes are classes that cannot be instantiated on their own, only extended.
public abstract class AbstractClass {

  protected double abstractDouble; //Protected means subclasses have access, but not outside classes

  public AbstractClass(double x) {
    this.abstractDouble = x;
  }

  //Can include complete methods
  public void absMethod() {
    System.out.println("Abstract method call");
  }

  //Or Abstract methods that must be implemented in subclasses
  public abstract double getDouble();
}
