#tuplas são dados combinados imutáveis
ingredientes = ("azeite", "sal", "vidro", "tomate infernal")
print(ingredientes)
print(ingredientes[-1])

#python possui a estrutura de lista
#não é um array, funciona mais parecido com um ArrayList sem tipagem
cardapio= ["feijoada", "pizza", "corvo", "maionese", "sangue de virgem", "animal critptideo assado"]
escolha = int(input("escolha seu prato:"))
print(f"humm delicioso {cardapio[escolha]}")
#-1 retorno o último elemento
print(f"nunca saboreei um {cardapio[-1]} tao gostoso")

#Dicionarios aninha elementos com suas respectivas chaves-> parece um HashMap<>
consulta = input('escolha uma magia para consultar:')
magias= {'fireball':'lança uma bola de fogo',
         'invisibilidade':'auto explicativa',
         'summon':'invoca algum mob aleatorio',
         'spirit':'invoca um espirito previamente adquirido'}
print(magias[consulta])


#tanto tuplas quanto listas e strings herdam a estrutura chamada "sequencia"
pizza = ["fermento","queijo", "margarita", "pimenta", "portuguesa", "carne", "frango", "cebola", "abacaxi"]
#slicing inclui o elemento do primeiro parâmetro mas não do segundo
fatiapicante = pizza[1:4]
print(fatiapicante)

malgosto= pizza[6:9]
print(malgosto)
#o terceiro parâmetro do slicing é o intervalo entre os valores selecionados
fatiarandom= pizza[0::2]
print(fatiarandom)
#o intervalo também recebe valores negativos
pizzareversa = pizza[::-1]
print(pizzareversa)

