public class Classes {

  private int instanceVariable; //Variable of each instance of the class (can be public, but frowned upone because of encapsulation)
  private InnerClass innerClass; //Classes can contain complex objects

  //Constructor with arguement
  public Classes(int x) {
    instanceVariable = x;
    innerClass = new InnerClass();
  }

  //Default constructor
  public Classes() {
    this(0); //Call other constructor
  }

  //Public method
  public int getInt() {
    return instanceVariable;
  }

  //Private method, can only be called from other class methods
  private void privMethod() {
    System.out.println("Private Method");
  }

  public void callPriv() {
    privMethod();
  }

  //Static methods don't need an isntance of the class
  public static void statMethod() {
    System.out.println("Static Method");
  }

  //Good practice to override the 'toString' method
  @Override
  public String toString() {
    return "Some string representation of the class";
  }

  //Classes can contain other classes, can only be instantiated from within this class
  private class InnerClass {
    public InnerClass() {
      System.out.println("Inner Class Created");
    }
  }



  //Test client
  public static void main(String[] args) {
    Classes defaultClass = new Classes(); //Default constructor
    System.out.println(defaultClass.getInt());

    Classes otherClass = new Classes(7);
    System.out.println(otherClass.getInt());

    otherClass.callPriv(); //Use a public method to access a private one

    Classes.statMethod(); //Static method, no instance needed

    System.out.println(otherClass); //Will use the toString method
  }

}

