//LABAY, KYLE ZANDER S.
//SILVA, JAN ALDRIN A.
//CCP 1102 - ITCB
//SMALLEST AND LARGEST ELEMENT USING ARRAY

import java.util.Scanner;
import java.util.InputMismatchException;
import java.text.NumberFormat;

public class SmallestAndLargestElement {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            try {
                System.out.println("Smallest and Largest Element in an Array");
                System.out.print("Enter size of array, [3 - 10] only: ");
                int size = scanner.nextInt();
                if (size < 3 || size > 10) {
                    System.out.println("Input error, input size of the array must not be less than 3 or greater than 10.\n");
                    scanner.nextLine();
                    continue;
                }
                int[] array = new int[size];
                System.out.println("Enter the " + size + " elements below");
                for (int i = 0; i < size; i++) {
                    try {
                        System.out.print("Enter element " + (i + 1) + ": ");
                        array[i] = scanner.nextInt();
                    }
                    catch (InputMismatchException e) {
                        System.out.println("Invalid input, element " + (i + 1) + " input must not be/have letters or special symbols.\n");
                        scanner.nextLine();
                        throw new Exception(); 
                    }
                }
                int smallestElement = array[0];
                int largestElement = array[0];
                for (int i = 1; i < size; i++) {
                    if (array[i] < smallestElement) {
                        smallestElement = array[i];
                    }
                    if (array[i] > largestElement) {
                        largestElement = array[i];
                    }
                }
                NumberFormat nf = NumberFormat.getInstance();
                System.out.println("Smallest element in the array set is " + nf.format(smallestElement) + ".");
                System.out.println("Largest element in the array set is " + nf.format(largestElement) + ".");
                break;
            }
            catch (InputMismatchException e) {
                System.out.println("Invalid input, input size of the array must not be/have letters or special symbols.\n");
                scanner.nextLine();
            }
            catch (Exception e) {
                continue;
            }
        }
    scanner.close();
    }
}