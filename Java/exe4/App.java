import java.io.IOException;

public class App {
    public static void clearScreen() throws IOException, InterruptedException {
        new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        // System.out.println("Hello, World!");

    }
    //Metodo
    public static int calcularFatorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Número deve ser não negativo.");
        } else if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * calcularFatorial(n - 1)
        }
    }

    public static void main(String[] args) throws Exception {
        clearScreen();
        int numero = 5;
        System.out.println("Fatorial de " + numero + " é: " + calcularFatorial(numero) + "\n\n");
    }
}