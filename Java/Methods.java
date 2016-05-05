public class Methods {

  public static void main(String[] args) {
    int x = 127;

    noParams();
    oneParam(x);
    System.out.println(x); //127

    System.out.println(toAdd(12, 43));
    System.out.println(toAdd(11.1, 11.1, 11.1));

  }

  //Void for no return type
  static void noParams() {
    System.out.println("No params");
  }

  //Primitive variables (and Strings) passed by value
  static void oneParam(int x) {
    x++;
    System.out.println(x); //128
  }

  //Specify which return type
  static int toAdd(int x, int y) {
    return (x+y);
  }

  //Overload function by changing signature
  //Can pass in a collection of undetermined size
  static double toAdd(double ... doubles) {
    double total = 0;
    for (double d : doubles) {
      total += d;
    }
    return total;
  }

}
