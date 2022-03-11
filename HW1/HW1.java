import static java.lang.Math.cos;
import java.io.PrintStream;
import java.io.IOException;

public class HW1 {
        public static void main(String args[]) throws IOException {
            // creates a file named equation.txt for saving our output
            PrintStream output = new PrintStream("hw1_lp.txt");
            System.setOut(output);

            // gets the total value that we need to maximize
            System.out.print("max: ");
            // double value = Math.floor(50 + 25 * cos(1));
//             System.setOut(output);
//             System.out.print(value + "x_{" + 1 +"} ");

            for (int i = 1; i <= 100; i++) {
                // gets value for each object
                double value = Math.floor(50 + 25 * cos(i));
                System.setOut(output);
                System.out.print("+ " + value + "x_{" + i +"} ");
            }
            System.setOut(output);
            System.out.println(";");

            // first constraint: weight <= 1000
            for (int j = 1; j <= 100; j++){
                // gets weight for each object
                double weight = Math.floor(30 + 12 * cos(4 * j + 1));
                System.setOut(output);
                System.out.print("+ " + weight + "x_{" + j + "} ");
            }
            System.out.println(" leq 300" + ";");
            // second constraint: volume <= 1000
            for (int k = 1; k <= 100; k++){
                // gets volume for each object
                double volume = Math.floor(30 + 12 * cos(2 * k + 2));
                System.out.print("+ " + volume + "x_{" + k + "} ");
            }
            System.out.println(" leq 300" + ";");

            // third constraint: all the x should be binary integer, 0 or 1
            System.setOut(output);
            System.out.print("bin ");
            for (int n = 1; n <= 99; n++){
                System.setOut(output);
                System.out.print("x_{" + n + "}, ");
            }
            System.setOut(output);
            System.out.print("x_" + 100 +";");
        }
}