# criando um jogo de acerto
from random import randint
# gerando um numero aleatorio de 0 ate 10
computador = randint(0, 10)
cont = 0
while True:
    # pedindo um numero até acertar
    jogador = int(input('Jogador: '))
    #contador de vezes para acertar
    cont += 1
    # se o jogador inserir o mesmo numero numero que o computador ele ganha
    if jogador == computador:
        break
    print('ERROU! Tente novamente.')  
# mostrando a quantidade de vezes levou para acertar o numeo  
print(f'A quantidade de vezes que pro jogador acertar foi: {cont}')

