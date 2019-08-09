public class ErrorHandling {

  public static void main(String[] args) {
    int[] someArray = new int[10];
    String someString = "Hi";

    try {
      //System.out.print(someArray[12]);

      //String sub = someString.substring(4);

      if (someArray.length < 20) {
       throw (new Exception("Array too short")); //Throw custom exception
      }

    } catch (ArrayIndexOutOfBoundsException e) { //There are many Exception types
      System.out.println("Not a valid array index");
    } catch (StringIndexOutOfBoundsException e) { //Can have multiple catch blocks
      System.out.println("Invalid substring index");
    } catch (Exception e) { //Handle custom exception
      System.out.println(e.getMessage());
    }

    System.out.println("This should still run");
  }
}
