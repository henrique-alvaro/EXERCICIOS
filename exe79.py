numeros = []
while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('Numero Adicionado com Sucesso')
    else:
        print('Numero Duplicado. Nao adicionado!')
    d = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    if d == 'N':
        break
print('-='*20)
numeros.sort()
print(f'Numeros {numeros} ordenados inscritos com Sucesso')
