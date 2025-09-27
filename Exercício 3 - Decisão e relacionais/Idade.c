#include <stdio.h>
int main () {
  
int idade;
printf("Digite sua idade: \n");
scanf("%d", &idade);
  
if(idade<18) {
  printf("Você é menor de idade.");
}
else {
  printf("Você é maior de idade.");
}
return 0;
}