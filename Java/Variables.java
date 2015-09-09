import java.math.BigDecimal;

public class Variables {

  public static void main(String[] args) {
    //Strictly typed

    //Primitves

    //Numerical
    byte a; //-128 to 127
    short b; //-32,768 to 32,767
    int x; //-2,147,483,648 to 2,147,483,647
    long z; //Unlimted range (within reason)
    x = 1;

    float q = 3.1f; //For precision
    double y = 2.0d; //Higher precision and range than float
    z = 213443l; //Note the 'l' after the dclaration


    System.out.println(x + "+" + y + "=" + (x+y)); //Automatic conversion
    System.out.println(x); //1
    x++;
    System.out.println(x); //2
    a = 127;
    System.out.println(a); //127
    a++;
    System.out.println(a); //-128

    //Primitves are always copies
    int val1 = 1;
    int val2 = val1;
    val1++;
    System.out.println(val1+" "+val2); //2 1

    long longVal = val1; //This is fine since it's casting to large primitive
    short shortVal = (short) val1; //Have to manually cast, can cause issues since smaller type

    //Math intro
    int divInt1 = 10;
    int divInt2 = 3;
    System.out.println(divInt1/divInt2); //3
    System.out.println(divInt1%divInt2); //1

    double divDoub1 = 10d;
    double divDoub2 = 3;
    System.out.println(divDoub1/divDoub2); //3.333......
    System.out.println(divDoub1%divDoub2); //1.0

    double toRound = -3.99;
    System.out.println(Math.round(toRound)); //-4
    System.out.println(Math.abs(toRound)); //3.99

    //Booleans
    boolean someBool = true; //true or false only

    //Characters
    char c1 = 'A'; //Note the SINGLE quotes
    System.out.println(c1); //A
    char c2 = '\u0024'; //Unicode
    System.out.println(c2); //$

    x = 5;
    System.out.println(++x); //6 (increment is done first)
    System.out.println(x++); //6 (increment is done after)
    System.out.println(x); //7
    x+=10;
    System.out.println(x); //17

    //Objects
    String name = "Bob";
    Integer myInt = 47;
    Byte myByte = 3;
    Short myShort = 12;

    System.out.println(name); //Bob
    System.out.println(myInt); //47

    //Big Decimal, more precise, use for financial transactions and such
    double someVal = .012d;
    double pSum = someVal + someVal + someVal;
    System.out.println(pSum);
    String strVal = Double.toString(someVal);

    BigDecimal bigVal = new BigDecimal(strVal);
    BigDecimal bSum = bigVal.add(bigVal).add(bigVal);
    System.out.println(bSum.toString());


  }

}
