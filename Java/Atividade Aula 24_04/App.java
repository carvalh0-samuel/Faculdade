import javax.swing.JOptionPane;

public class App {

    public static void main(String[] args) throws Exception {
        
        try {
            //entrada do valor inicial
            String entrada = JOptionPane.showInputDialog("Informe o valor inicial:");
            Double valorinicial = Double.parseDouble (entrada);
            
            //valida se o valor é maior que 0
            if (valorinicial < 0) {
                JOptionPane.showMessageDialog(null, "Erro: O valor inicial não pode ser negativo.");
                return;
            }
            //calcula o valor da multa e soma ao valor inicial
            Double valormulta = valorinicial * 0.32;
            Double valortotal = valorinicial + valormulta;

            
            String mensagem = String.format(
                "A - Valor inicial: R$ %.2f\n" +
                "B - Valor da Multa: R$ %.2f\n" +
                "C - Valor total: R$ %.2f",
                valorinicial, valormulta, valortotal
            );

            JOptionPane.showMessageDialog(null, mensagem);

        //tratamento de erro caso o usuário digite letras
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Erro: insira um número válido.");
        }
    }
}