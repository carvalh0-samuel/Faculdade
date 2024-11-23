#include <stdio.h>

int main(){
    float nota1,nota2,nota3;
    float media;
    printf("Digite suas notas:");
    scanf("%f,%f,%f",&nota1,&nota2,&nota3);
    
    media=(nota1+nota2+nota3)/3;
    printf("Sua media e:%f\n",media);
    return 0;
}
