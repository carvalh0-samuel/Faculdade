import java.io.IOException;
import java.util.Scanner;

public class App {
     public static void clearScreen() throws IOException, InterruptedException {
        new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
    }
    public static void main(String[] args) throws Exception {
        clearScreen();
        Scanner scan = new Scanner(System.in); // Criando objetos
       try {
          System.out.print("Informe um valor inteiro: ");
          int valor = scan.nextInt();
          int total = valor /1;
        } catch (ArithmeticException e) {
            // Código para tratar a exceção
            System.out.println("\n\nErro: Divisão por zero.\n\n");
        } finally {
            // Código que executa sempre, com ou sem erro
            System.out.println("\n\nFinalizado com sucesso.\n\n");
        }
    }
}
