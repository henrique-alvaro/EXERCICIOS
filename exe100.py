from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 numeros: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.4)
    print('Fim')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores de {lista}, temos {soma}')
            
    
numeros = list()
sorteio(numeros)
somapar(numeros)