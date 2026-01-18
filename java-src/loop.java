public class loop {
    public static void main(String[] args) {
        int number = 3;
        int anotherNumber = 5;
        for (int counter = 15; counter >= 11; counter--) {
            anotherNumber = anotherNumber + counter;
            number = number + anotherNumber;
            System.out.println(number);
        }
    }
}
