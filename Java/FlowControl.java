public class FlowControl {

  public static void main(String[] args) {

    int x = 0;
    int y = 1;

    //Basic if
    if (x != y) {
      System.out.println("They are not equal");
    } else {
      System.out.println("They are equal");
    }

    //Ternary shorthand
    String result = (x == y) ? "They are equal" : "They are not equal";
    System.out.println(result);

  }

}
