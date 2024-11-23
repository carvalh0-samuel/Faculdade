#include <stdio.h>

int main() {
    int base,altura,area;
    
    printf("Digite o valor da base e da altura:");
    scanf("%i,%i",&base,&altura);
    
    area=(base*altura)/2;
    printf("A area do triangulo e:%i\n",area);
    return 0;
}