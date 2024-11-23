#include <stdio.h>

int main() {
    float nota1, nota2, media;
    char nome[50]; 

    printf("Digite seu nome: ");
    scanf("%99[^\n]", nome);

    printf("Digite a primeira nota: ");
    scanf("%f", &nota1);
    
    printf("Digite a segunda nota: ");
    scanf("%f", &nota2);

    media = (nota1 * 0.4) + (nota2 * 0.6);
    media = media / 2;

    printf("Seu nome é %s e sua média é %.2f\n", nome, media);
    
    return 0;
}