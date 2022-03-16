lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c}° valor: ')))
    if c == 0:
        maior = menor = lista[0]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor e {maior} é está na posiçao: ', end='')
for c, l in enumerate(lista):
    if l == maior:
        print(f'{c}°', end=' ')
print()
print(f'O menor valor e {menor} é estar na posiçao: ', end='')
for c, l in enumerate(lista):
    if l == menor:
        print(f'{c}°', end=' ')


