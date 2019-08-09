import java.util.*;

public class OOTester {
  public static void main(String[] args) {
    //No import needed since in same directory
    Classes defaultClass = new Classes(); //Default constructor
    System.out.println(defaultClass.getInt());

    Classes otherClass = new Classes(7);
    System.out.println(otherClass.getInt()); //Public method
    System.out.println(otherClass.getDouble()); //Public method

    otherClass.callPriv(); //Use a public method to access a private one
    otherClass.absMethod(); //Method in abstract superclass

    Classes.statMethod(); //Static method, no instance needed

    System.out.println(otherClass); //Will use the toString method

    System.out.println();

    Inheritance subClass = new Inheritance("Bob", 47);
    System.out.println(subClass.getString()); //Subclass method
    System.out.println(subClass.getInt()); //Superclass method
    System.out.println(subClass); //Overriden method

    //Collections can use inherited classes
    List<Classes> someList = new ArrayList<>();
    someList.add(otherClass);
    someList.add(subClass);


  }
}
