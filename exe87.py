matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somacoluna = maiorlinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um numero para [{l}, {c}]'))
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
    print()
print('-='*20)
print(f'A soma de todos os valores pares é: {somapares}')
for l in range(0, 3):
    somacoluna += matriz[l][2]
print(f'A Soma dos valores da 3° coluna é: {somacoluna}')
for c in range(0, 3):
    if c == 0:
        maiorlinha = matriz[1][c]
    else:
        if matriz[1][c] > maiorlinha:
            maiorlinha = matriz[1][c]
print(f'O maior numero da 2° linha é: {maiorlinha}')
