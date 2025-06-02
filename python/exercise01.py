#calcular soma e média de números em uma lista
numeros = [3, 20, 31, 17, 26, 69, 3.2, 666.777, 420, 5,]
#função sum(numeros)
soma=0
maximo = numeros[0]
for valor in numeros:
  soma+=valor
  if valor>maximo:
    maximo=valor
media= soma/len(numeros)

print(f'A soma dos valores é: {soma}')
print(f'o valor mais alto da lista é: {maximo}')
print(f'A média da lista é: {media}')

#checar valores entre listas
omega = [12, 'Jiboia',soma, maximo, 'diferencial', 1200]
alfa= [0, 'cobra', 666.777, 1260.977, 1200]

for elemento in omega:
  for dado in alfa:
    if elemento == dado:
      print(f'{elemento} é um dado duplicado')

