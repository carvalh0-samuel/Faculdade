#include <stdio.h>
#include <stdlib.h>

int main()
{
    int vetor[15];
    int i;
    
    for(i=0; i<15; i++){
        
        printf("Digite valores: ");
        
        scanf("%d" , &vetor[i]);
}
  int soma;
  for(i=0; i<15; i++){
      
      soma=soma+vetor[i];
      printf("Resultado da soma dos vetores: %d \n" , soma);
  }
  
  int final=soma/15;
  
  printf("\nResultado da media: %d " , final);
  
    return 0;
}