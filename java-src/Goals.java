import java.util.Scanner;

public class Main {
    public static void main(String []args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of players: ");
        int playerAmount = scanner.nextInt();
        int[] numberOfPlayers = new int[playerAmount];
        int maxGoals = 0;
        for (int i = 0; i < playerAmount; i++) {
            System.out.print("Goals score by player #" + (i + 1) + ": ");
            numberOfPlayers[i] = scanner.nextInt();
            if (numberOfPlayers[i] > maxGoals) {
                maxGoals = numberOfPlayers[i];
            }
        }
        if (maxGoals > 10) {
            System.out.println("Not Messi");
        } else {
            System.out.println("Okay, fine, it's Messi");
        }
        scanner.close();
    }
}