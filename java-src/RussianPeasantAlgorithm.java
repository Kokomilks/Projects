import java.util.Scanner;

public class RussianPeasantAlgorithm {
    static Scanner scanner = new Scanner(System.in);
    public static int algorithm() {
        System.out.print("Enter a multiplicand: ");
        int multiplicand = scanner.nextInt();
        System.out.print("Enter a multiplier: ");
        int multiplier = scanner.nextInt();
        int finalMultiplier = 0;
        while(multiplicand > 0) {
            if(multiplicand % 2 != 0) {
                finalMultiplier += multiplier;
            }
            multiplicand /= 2;
            multiplier *= 2;
        }
        return finalMultiplier;
    }
    public static void main(String[] args) {
        clearTerminal.clear();
        System.out.println("---Russian Peasant Algorithm---");
        System.out.println("The product is " + algorithm());
    }
}