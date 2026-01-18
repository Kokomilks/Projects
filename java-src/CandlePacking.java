import java.util.InputMismatchException;
import java.util.Scanner;

public class CandlePacking {
    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        int candleDiameter = 0;
            try {
                System.out.print("Enter diameter of candle: ");
                candleDiameter = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Invalid input, diameter input must not be letters or special symbols.");
                System.exit(0);
            }
            if (candleDiameter != 1 || candleDiameter != 2) {
                System.out.println("Input error, diameter input must be 1 or 2 only.");
                System.exit(0);
            }
        int oneDimension = 0;
            try {
                System.out.print("Enter dimension one value: ");
                oneDimension = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Invalid input, dimension one input must not be letters or special symbols.");
                System.exit(0);
            }
            if (oneDimension < 1) {
                System.out.println("Input error, dimension one input must not be less than 1.");
                System.exit(0);
            }
        int twoDimension = 0;
            try {
                System.out.print("Enter dimension two value: ");
                twoDimension = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Invalid input, dimension two input must not be letters or special symbols.");
                System.exit(0);
            }
            if (twoDimension < 1) {
                System.out.println("Input error, dimension two input must not be less than 1.");
                System.exit(0);
            }
    }
}