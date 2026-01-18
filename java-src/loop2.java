public class loop2 {
    public static void main(String[] args) {
        int number = 10;
        int anotherNumber = 2;
        for (int counter = 10; counter >= 5; counter--) {
            number = number * 2;
            anotherNumber = anotherNumber * 2;
            System.out.println(counter - number % anotherNumber);
        }
    }
}