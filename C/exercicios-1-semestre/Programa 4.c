#include <stdio.h>

int main() {
   int numero1,numero2,numeroT;
   
   printf("Digite dois numeros:");
   scanf("%i,%i",&numero1,&numero2);
   
   numeroT=numero1;
   numero1=numero2;
   
   printf("Seus numeros sao:%i,%i",numero1,numeroT);
   return 0;
}