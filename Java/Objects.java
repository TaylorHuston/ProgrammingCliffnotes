public class Objects {

  public static void main(String[] args) {

    //Objects
    String name = "Bob";
    Integer myInt = 47;
    Byte myByte = 3;
    Short myShort = 12;

    System.out.println(name); //Bob
    System.out.println(myInt); //47

    //Strings have a lot of helper functions
    System.out.println(name.length()); //3
    String s1 = name+"by";
    System.out.println(s1); //Bobby
    String s2 = s1+" loves chicken";
    System.out.println(s2); //Bobby loves chikcen

    char[] hello = {'H', 'e', 'l', 'l', 'o'};
    String s3 = new String(hello);
    System.out.println(s3); //Hello

    char[] chars = s3.toCharArray();
    System.out.println(chars); //Hello

    for (char c : chars) { //Each looop
      System.out.println(c);
    }

  }
}
