# criando um jogo de adivinha
from random import randint
from time import sleep
# fazendo o computador sortear um numero de 0 ate 5
cpu = randint(0, 5)
print('<< TENTE ADIVINHAR >>')
# pedindo qual numero o jogador vai jogar
jogador = int(input('Jogador tente adivinhar o numero entre (0, 5): '))
# analisando se o jogador acertou ou nao o numero
if jogador == cpu:
    print('ACERTOU')
    sleep(0.5)
    print(f'Computador jogou {cpu} e o Jogador jogou {jogador}')
else:
    print('ERROU')
    sleep(0.5)
    print(f'Computador jogou {cpu} e o Jogador jogou {jogador}')