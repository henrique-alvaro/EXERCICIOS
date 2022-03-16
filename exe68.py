from random import randint
print('<<< JOGO DE PAR ou IMPAR >>>')
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou IMPAR [P/I]: ')).strip().upper()[0]
    print(f'Jogador jogou {jogador}, computador jogou {computador}, total {total}', end='')
    print(f' DEU IMAPAR' if total % 2 == 1 else ' DEU PAR')
    if tipo == 'P':
        if total % 2 == 0:
            print(f'VOCE GANHOU')
        else:
            print(f'VOCE PERDEU')
            break
    else:
        if total % 2 == 1:
            print('VOCE GANHOU')
        else:
            print('VOCE PERDEU')
            break

