print("interpretador python instalado com sucesso!")
print("essa linguagem não tem compilador - paia")

fluxo = int(input('escolha um teste de 0 a 3'))

if fluxo == 0:
  print("a identação do python é estranha pra carai")
elif fluxo > 3:
  print("você é burro?")
else:
  print("escolha é uma ilusão")
  user= input("digite outra parada")
  print("fun fact- o input sempre lê a entrada como string")
  print(str(type(user)) + user)

#formatação de texto com python
format= "texto-intruso"
print(f"essa string é formatada com chaves: {format}")
seila= 2.756488
naosei= 66.7770777
print(f"esse numero tem 3 casas decimais: {seila:.3f}\ne esse tem todas: {naosei}")
print(r"usar\raw\na\string\é\útil\qnd\se\tem\muitas\barras\tipo\filepath")
