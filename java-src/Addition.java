import java.util.Scanner;
public class Addition {
    public static void compute(int firstNumber, int secondNumber) {
        int sum;
        sum = firstNumber + secondNumber;
        System.out.println("The sum is " + sum + ".");
    } 

    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        int firstValue;
        int secondValue;

        System.out.println("Addition");
        try {
            System.out.print("Enter first number: ");
            firstValue = scanner.nextInt();
            try {
                System.out.print("Enter second number: ");
                secondValue = scanner.nextInt();
                compute(firstValue, secondValue);
            } catch(Exception e) {
                System.out.println("Invalid input, second number must not be/have letters or special symbols.");
            }
        } catch(Exception e) {
            System.out.println("Invalid input, first number must not be/have letters or special symbols.");
        }
    }
}