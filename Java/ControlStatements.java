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

    x = 0;
    //Switch
    switch (x) {
      case 0:
        System.out.println("This should be ran");
        break;
      case 1:
        System.out.println("This won't be ran");
        break;
      default:
        System.out.println("This would be ran if none of the other conditions were met");
        break;
    }

    int[] someArray = {1,2,3,4,5,6,7,8,9};

    //For
    for (int i=0; i < someArray.length; i++) {
      System.out.print(someArray[i]);
    }
    System.out.println();
    //For, colletions only
    for (int z : someArray) {
      System.out.print(z);
    }
    System.out.println();

    //While
    int i = 0;
    while (i < someArray.length) {
      System.out.print(someArray[i]);
      i++;
    }
    System.out.println();

    //Do-While
    i = 0;
    do {
      System.out.print(someArray[i]);
      i++;
    } while (i < someArray.length);
  }
}
