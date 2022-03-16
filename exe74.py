from random import randint
maior = menor = 0
for c in range(1, 6):
    valores = randint(1, 9)
    print(valores, end=' ')
    if c == 1:
        maior = menor = valores
    else:
        if valores > maior:
            maior = valores
        if valores < menor:
            menor = valores
print()
print(f'O maior valor e {maior} é menor valores e {menor}')