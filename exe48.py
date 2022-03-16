# criando uma somatoria de numeros impares multiplos de 3
soma = 0
cont = 0
# fazendo o calculo dos numeros impares multiplos de 3 
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'Total de valores solicitados são: {cont}')
print(f'A soma de todos os valores solicitados e: {soma}')

