package java_program;
import java.util.Scanner;

public class RussianPeasantAlgorithm {
    public static void clear() {
    System.out.print("\033[H\033[2J");
    System.out.flush();
    }

    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        clear();
        int multiplicand;
        System.out.print("Enter a multiplicand: ");
        multiplicand = scanner.nextInt();

        /*int multiplier;
        System.out.println("Enter a multiplier: ");
        multiplier = scanner.nextInt();*/
        
        for(; multiplicand != 1;) {
            multiplicand = (int) Math.floor(multiplicand / 2);
            System.out.println(multiplicand);
        }
    }
}