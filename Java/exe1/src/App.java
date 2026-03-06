public class App {
    public static void main(String[] args) throws Exception {
        int a = 112;
        int b = 222;
        int c = 332;

        if (a>b && a>c) {
            System.out.println("O valor: "+ a +", que esta em A, e maior");
        }
        else if (b>a && b>c){
            System.out.println("O valor: "+ b +", que esta em B, e maior"); 
        }
        else if (c>a && c>b){
            System.out.println("O valor: "+ c +", que esta em C, e maior");
        }
        else {
            System.out.println("Todos sao iguais");
        }
    }
}