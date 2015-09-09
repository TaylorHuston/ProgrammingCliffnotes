import java.text.NumberFormat;
import java.util.Date;
import java.time.LocalDateTime;
import java.time.LocalDate;

public class Objects {

  public static void main(String[] args) {

    //Objects
    String name = "Bob";

    //Primitives have Object wrappers that have helper functions
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
    System.out.println(s2); //Bobby loves chicken

    System.out.println(s2.indexOf("loves")); //6
    System.out.println(s2.substring(6)); //loves chicken

    char[] hello = {'H', 'e', 'l', 'l', 'o'};
    String s3 = new String(hello);
    System.out.println(s3); //Hello

    char[] chars = s3.toCharArray();
    System.out.println(chars); //Hello

    for (char c : chars) { //Each looop
      System.out.println(c);
    }

    int someInt = 42;
    String fromInt = Integer.toString(someInt);
    System.out.println(fromInt); //42

    boolean someBool = true;
    String fromBool = Boolean.toString(someBool);
    System.out.println(fromBool); //true

    //StringBuilder allows you to not need to create multpiple String objects
    StringBuilder sb = new StringBuilder("Hello");
    sb.append(" world");
    System.out.println(sb); //Hello world

    s1 = "Hello";
    s2 = "Hello";
    System.out.println(s1==s2); //True, but can be deceiving
    System.out.println(s1.equals(s2)); //True, and better


    //Number Format can format strings based on locale and language
    double doubVal = 1_234_567.89;
    String doubString = Double.toString(doubVal);
    System.out.println(doubString);

    NumberFormat numF = NumberFormat.getNumberInstance();
    System.out.println(numF.format(doubVal));

    NumberFormat curF = NumberFormat.getCurrencyInstance();
    System.out.println(curF.format(doubVal));

    s1 = "9876543.21";
    doubVal = Double.parseDouble(s1);
    System.out.println(doubVal);

    //Dates
    Date d = new Date(); //Current time
    System.out.println(d);

    //Java 8 only
    LocalDateTime ldt = LocalDateTime.now();
    System.out.println(ldt);

    LocalDate ld = LocalDate.of(2009, 1, 28);
    System.out.println(ld);

  }
}
