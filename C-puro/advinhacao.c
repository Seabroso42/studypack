//import
#include <stdio.h>
#include <stdlib.h>

//declaração de constantes
#define PONTOSINICIAIS 500

int main() {

  printf("**********************************\n");
  printf("* primeiro programa escrito em C *\n");
  printf("**********************************\n");

  int numerosecreto = 21;
  int chute;

  int tentativa= 1;
  double pontopartida= PONTOSINICIAIS;


  printf("o computador está scolhendo um número secreto...\n");

  while(1){
     printf("Digite o número que você pensa que é: ");
    scanf("%d", &chute);

    int maior = chute > numerosecreto;
    int menor = chute < numerosecreto;

    if(chute<0){
      printf("não pode chutar números negativos\n");
      tentativa--;
      continue;
    }

    else if(chute == numerosecreto) {
    printf("Parabéns! Você acertou na %d tentativa!\n", tentativa);
    printf("Pontuação: %.1f", pontopartida);
    printf("Jogue de novo, você é um bom jogador!\n");
    break;
  }
  else {
    printf("Tentativa %d\nVocê errou!\n", tentativa);

    double diferenca;

    if(maior){
      printf("o chute de %d foi um número muito alto.\n", chute);
      diferenca= chute - numerosecreto;
    }
    if(menor){
      printf("o chute de %d foi um número muito baixo.\n", chute);
      diferenca= numerosecreto - chute;
    }
    pontopartida= pontopartida - diferenca/2;
    printf("você perdeu %.1f pontos", pontopartida);
  }
  if(pontopartida == 0){
    printf("FIM DE JOGO\nO número secreto é: %d\n", numerosecreto);
    break;
  }

  }

}

