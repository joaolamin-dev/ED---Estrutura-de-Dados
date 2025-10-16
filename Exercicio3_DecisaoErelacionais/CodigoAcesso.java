import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
      Scanner codigo = new Scanner (System.in);
    
      System.out.println("Digite o código de acesso: ");
      String codigoacesso = codigo.nextLine();
      
      if(codigoacesso.equals("Admin123")) {
        System.out.println("Bem-vindo, Administrador!");
      }
      else if(codigoacesso.equals("User123")) {
        System.out.println("Bem-vindo, Usuário!");
      }
      else {
        System.out.println("Código Incorreto.");
      }
  }
}