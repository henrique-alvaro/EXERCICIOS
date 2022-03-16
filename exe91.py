from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
rankings = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for c, l in enumerate(ranking):
    print(f'{c+1}° lugar {l[0]} com {l[1]}')
    sleep(1)