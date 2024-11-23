#include <stdio.h>
int main(){
    float nota1, nota2, media;
 
    printf("Digite a primeira nota:\n");
    scanf("%f", &nota1);
    printf("Digite a segunda nota:\n");
    scanf("%f", &nota2);
    media = (nota1 + nota2)/2;
 
    if (media >= 6){
       printf("Está Aprovado");
    }else{
       printf("Está Reprovado");
    }
    return 0;
}