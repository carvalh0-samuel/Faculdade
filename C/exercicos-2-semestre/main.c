#include <stdio.h>
#include <string.h>

// Definição da estrutura deve estar fora da função main
struct ItemBiblioteca {
    char titulo[100];
    char autor[100];
    int anoPublicacao;
    char tipoMidia[10];
};

int main() {
    int i;
    struct ItemBiblioteca biblioteca[100];
    int numItens = 0;

    // Adicionando um livro na biblioteca
    strcpy(biblioteca[numItens].titulo, "O Senhor dos Anéis");
    strcpy(biblioteca[numItens].autor, "J. R. R. Tolkien");
    biblioteca[numItens].anoPublicacao = 1937; // Correção aqui
    strcpy(biblioteca[numItens].tipoMidia, "Livro");
    numItens++;
    
    // Adicionando uma revista na biblioteca
    strcpy(biblioteca[numItens].titulo, "National Geographic");
    strcpy(biblioteca[numItens].autor, "Vários");
    biblioteca[numItens].anoPublicacao = 2001; // Correção aqui
    strcpy(biblioteca[numItens].tipoMidia, "Revista");
    numItens++;
    
    // Exibindo os itens na biblioteca
    for (i = 0; i < numItens; i++) { // Correção aqui para usar numItens
        printf("Título: %s\n", biblioteca[i].titulo);
        printf("Autor: %s\n", biblioteca[i].autor); // Correção aqui
        printf("Ano da Publicação: %d\n", biblioteca[i].anoPublicacao); // Correção aqui
        printf("Tipo de Mídia: %s\n", biblioteca[i].tipoMidia);
        printf("\n"); // Linha em branco para separar os itens
    }
    
    return 0;
}
