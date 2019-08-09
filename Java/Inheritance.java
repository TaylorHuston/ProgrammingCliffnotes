//Single inheritance only
//Tests are in OOTester.java
public class Inheritance extends Classes {

  private String instanceString;

  public Inheritance(String instanceString, int newInt) {
    super(newInt); //Call superclass constructor
    this.instanceString = instanceString; //this is needed
  }

  //Subclass specific method
  public String getString() {
    return instanceString;
  }

  //Override Superclass method
  @Override
  public String toString() {
    return "Some string representation of the subclass";
  }

}
