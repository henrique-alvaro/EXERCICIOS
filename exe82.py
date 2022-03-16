numeros = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um numero: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    d = ' '
    while d not in 'SN':
        d = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    if d == 'N':
        break
print(f'Lista com todos os numeros inscritos: {numeros}')
print(f'Listas com todos numeros Pares: {pares}')
print(f'Lista com todos os numeros Impares: {impares}')
