#include <stdio.h>

int main (){
	int a,b;
	printf("Digite o primeiro número:");
	scanf("%i",&a);
	
	printf("Digite o segundo número:");
	scanf("%i",&b);
	
	if (a/b<=b) {
		printf("o primeiro número e menor que o segundo");
	} else {
		printf("o segundo número e menor que o primeiro");
	}
	return 0;
}