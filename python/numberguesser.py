jogar = True
while jogar== True:
  segredo= int(input("desafiante- escolha um número:"))
  print("numero escolhido agora é a hora do desafiado")
  tentativas= 5
  #função range usada para iteração
  for _ in range(tentativas):
    chute = int(input("tenta a sorte menor: "))
    if chute < segredo:
      print("muito baixo corno")
    elif chute > segredo:
      print("muito alto otario")
    else:
      print("acertou mizeravi")
      break
  print("acabaram as tentativas")
  jogar = input("você quer continuar a jogar? s/n: ") == 's'

print("obrigado por perder seu tempo aqui")