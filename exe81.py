numeros = list()
while True:
    numeros.append(int(input('Digite um numero: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Teve um total de {len(numeros)} numeros')
o = sorted(numeros, reverse=True)
print(f'Numeros {o} ordenaods de forma decrescente')
if 5 in numeros:
    print('O numeros 5 foi digitado')
else:
    print('O numeros 5 nao foi digitado')