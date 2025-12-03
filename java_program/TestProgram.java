package java_program;

public class TestProgram {
    
    public static void clear() {
    System.out.print("\033[H\033[2J");
    System.out.flush();
    }
    public static void main(String[] args) {
        clear();
        System.out.println("Test String");
    }
    
}