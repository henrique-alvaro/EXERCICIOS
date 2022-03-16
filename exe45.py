# sorteando 3 numeros e aplicando ao pedra, papel e tesoura
from random import randint
from time import sleep
# com os numeros gerando jogo de pedra, tesoura
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
# jogador escolhendo sua jogada
print('''Escolha sua Opçao
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')
jogador = int(input('Jogador: '))
sleep(1.5)
print('-='*20)
# mostrando a jogada do computadore e do jogador
print(f'Computador escolheu: {computador}')
print(f'Jogador escolheu: {jogador}')
print('-='*20)
sleep(0.5)
# analisando se jogador perdeu, ganhou ou empatou
if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('Opção invalida')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('Opção invalida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATOU')
    else:
        print('Opção invalida')
else: 
    print('Opção invalida')