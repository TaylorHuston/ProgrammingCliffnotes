//Examples of some boolean logic
public class Boolean {

    public static void main(String args[]) {
        int num1 = 100;
        int num2 = 50;

        if (num1 == 100 && num2 == 50) { //Both are true
            System.out.println("True");
        }

        if (num1 == 100 || num2 == 50) {  //Either are true
            System.out.println("True");
        }

        if ((num1 == 100) & (num2 == 50)) {  //Both are true, and always evaluates both expressions
            System.out.println("True");
        }

        if ((num1 == 100) | (num2 == 50)) {  //Either is true, and always evaluates both expressions
            System.out.println("True");
        }

        if ((num1 == 100) ^ (num2 == 50)) {  //True if one is true and the other is false
            System.out.println("False");
        }

        if (! (num1 == 100)) {  //Negation
            System.out.println("False");
        }

        if (num1 != 100) {  //Not equal
            System.out.println("False");
        }

    }

}