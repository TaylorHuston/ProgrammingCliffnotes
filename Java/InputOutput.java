import java.util.Scanner;

public class InputOutput {
  
  public static void main(String[] args) {
    System.out.print("Hello ");
    System.out.println("world");

    Scanner in = new Scanner(System.in);
    System.out.print("Value: ");

    String fromConsole = in.nextLine();
    System.out.println("Your input was: "+fromConsole);

    System.out.print("A Double: ");
    Double newDbl = in.nextDouble(); //Will throw and error if not a numeric value
    System.out.println("Your input was: "+newDbl);

  }
  
}
