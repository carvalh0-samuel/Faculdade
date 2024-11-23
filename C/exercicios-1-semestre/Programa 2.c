#include <stdio.h>

//declara a constante pi//
#define PI 3.14

int main() {
    float raio;
    float area;
    printf("Digite o raio do circulo:");
    scanf("%f",&raio);
    
    area=PI*raio*raio;
    printf("A area do circulo e:%f\n",area);
    return 0;
}
