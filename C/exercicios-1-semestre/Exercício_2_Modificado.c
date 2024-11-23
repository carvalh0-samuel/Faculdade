#include <stdio.h>

int main() {
	int num;
	printf("Digite um número:");
	scanf("%i",&num);
	
	if (num%2==0 && num!=2) {
		printf("Seu numero e par, porem nao e primo");
		
	} else {
	    printf("seu numero tem altas chance de ser primo");
	}
	return 0;

}

