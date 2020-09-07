import java.io.*;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;


public class FileIO {
 
  public static void main(String[] args) {
    File inputFile = new File("data.txt");
    ArrayList<String> answers = new ArrayList<String>();

    //Must always use a Try-Catch block when doing file IO
    try {
      Scanner input = new Scanner(inputFile);

        while (input.hasNextLine()) {
            answers.add(input.nextLine());
        }

        System.out.print(answers);
        } catch (Exception e) {

        }

      File outputFile = new File("output.txt");
      try {
        PrintWriter out = new PrintWriter(outputFile);
        out.println("Banananana");
        out.close();
      } catch (Exception e) {

    }
  }
  
}
